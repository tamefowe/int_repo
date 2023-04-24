
import sys
import csv
import argparse
from statistics import median
from collections import defaultdict


class InvalidValueError(Exception):
    pass


class DataProcessor(object):
    _added_headers = ['SymbolBought', 'SymbolSold', 'SymbolPosition', 'SymbolNotional',
                      'ExchangeBought', 'ExchangeSold', 'TotalBought', 'TotalSold',
                      'TotalBoughtNotional', 'TotalSoldNotional', '\n']
    _cache = dict(
        Trades=dict(Processed_Trades=0, Shares=dict(Bought=0, Sold=0), Total_Volume=0,
                    Notional=dict(Bought=0.00, Sold=0.00)),
        Per_Exchange_Volumes=defaultdict(dict),
        Symbols=defaultdict(dict),
        Sizes=defaultdict(dict)
    )

    def __init__(self, input_file_name: str, output_file_name: str, chunk_size: int = 100) -> None:
        self._input_file_name = input_file_name
        self._output_file_name = output_file_name
        self._chunk_size = chunk_size

    def _enrich_trade(self, trade: str) -> tuple:
        localtime, symbol, event_type, side, fill_size, fill_price, fill_exchange = trade
        size = int(fill_size)
        price = float(fill_price)
        side_type = 'Sold' if side in ['s', 't'] else 'Bought'

        self._cache['Trades']['Processed_Trades'] += 1
        self._cache['Trades']['Total_Volume'] += size

        other_side_type = list({'Bought', 'Sold'} - {side_type})[0]
        self._cache['Trades']['Shares'][side_type] += size
        self._cache['Trades']['Notional'][side_type] += (size * price)

        # to get size per exchange
        if fill_exchange not in self._cache['Per_Exchange_Volumes']:
            self._cache['Per_Exchange_Volumes'][fill_exchange][side_type] = size
            self._cache['Per_Exchange_Volumes'][fill_exchange][other_side_type] = 0
        else:
            self._cache['Per_Exchange_Volumes'][fill_exchange][side_type] += size

        # to get size per symbol
        if symbol not in self._cache['Symbols']:
            self._cache['Symbols'][symbol][side_type] = size
            self._cache['Symbols'][symbol][other_side_type] = 0
        else:
            self._cache['Symbols'][symbol][side_type] += size

        # to find median
        if size not in self._cache['Sizes']:
            self._cache['Sizes'][size] = 1
        else:
            self._cache['Sizes'][size] += 1

        result = [
            localtime, symbol, event_type, side, fill_size, fill_price, fill_exchange,
            self._cache['Symbols'][symbol]['Bought'],
            self._cache['Symbols'][symbol]['Sold'],
            (self._cache['Symbols'][symbol]['Bought'] - self._cache['Symbols'][symbol]['Sold']),
            size * price,
            self._cache['Per_Exchange_Volumes'][fill_exchange]['Bought'],
            self._cache['Per_Exchange_Volumes'][fill_exchange]['Sold'],
            self._cache['Trades']['Shares']['Bought'],
            self._cache['Trades']['Shares']['Sold'],
            self._cache['Trades']['Notional']['Bought'],
            self._cache['Trades']['Notional']['Sold']
        ]

        return tuple(result)

    def _get_chunked_trades(self, trades):
        chunk = []

        for line in trades:
            chunk.append(line)
            if len(chunk) == self._chunk_size:
                yield chunk
                chunk = []

        if chunk:
            yield chunk

    @staticmethod
    def _is_trade_valid(trade):
        try:
            fill_size, fill_price, side, event_type, exchange, symbol = \
                trade[4], trade[5], trade[3], trade[2], trade[6], trade[1]
        except IndexError:
            print('Missing side, fill size/price, exchange!', file=sys.stderr)
            return False

        if event_type != 'TRADE':
            print('Not considering event type {}'.format(event_type), file=sys.stderr)
            return False
        try:
            _ = int(fill_size)
            _ = float(fill_price)
            if side not in ['b', 't', 's']:
                raise InvalidValueError
        except InvalidValueError:
            print('Invalid data for fill size {} or fill price {} or side {}'.format(fill_size, fill_price, side),
                  file=sys.stderr)
            return False
        return True

    def _get_output_summary(self):
        summary = \
            """\
WITHOUT PANDAS
---------------

Processed Trades: %s


Shares Bought: %s
Shares Sold: %s
Total Volume: %s
Notional Bought: %s
Notional Sold: %s


Per Exchange Volumes:
%s

Average Trade Size: %s
Median Trade Size: %s 


10 Most Active Symbols: %s
            """
        per_exchange_volume_str = ''
        for exchange, side_sizes in sorted(self._cache['Per_Exchange_Volumes'].items()):
            for side, size in sorted(side_sizes.items()):
                per_exchange_volume_str += '%s %s: %s\n' % (exchange, side, '{:,d}'.format(size))

        all_trades = list()
        for size, occur in self._cache['Sizes'].items():
            all_trades += ([size] * occur)

        median_trade_size = int(median(all_trades))

        symbol_sizes = dict()
        for symbol, sides in self._cache['Symbols'].items():
            symbol_sizes[symbol] = sum(sides.values())

        most_active_symbols = [(sym, symbol_sizes[sym]) for sym in
                               sorted(symbol_sizes, key=symbol_sizes.get, reverse=True)]
        most_active_symbols_str = \
            ', '.join(
                ['%s(%s)' % (sym, '{:,d}'.format(size)) for i, (sym, size) in enumerate(most_active_symbols) if i < 10])

        args = [
            '{:,d}'.format(self._cache['Trades']['Processed_Trades']),
            '{:,d}'.format(self._cache['Trades']['Shares']['Bought']),
            '{:,d}'.format(self._cache['Trades']['Shares']['Sold']),
            '{:,d}'.format(self._cache['Trades']['Total_Volume']),
            '${:0,.2f}'.format(self._cache['Trades']['Notional']['Bought']),
            '${:0,.2f}'.format(self._cache['Trades']['Notional']['Sold']),
            per_exchange_volume_str,
            '${:0,.2f}'.format(self._cache['Trades']['Total_Volume'] / self._cache['Trades']['Processed_Trades']),
            '{:,d}'.format(median_trade_size),
            most_active_symbols_str
        ]

        print(summary % tuple(args))

    def process_data(self) -> None:
        try:
            with open(self._input_file_name) as readhandler, open(self._output_file_name, 'w') as writehandler:
                trades = csv.reader(readhandler, delimiter=',')
                header = next(trades)
                writehandler.write(','.join(header + self._added_headers))

                for chunk in self._get_chunked_trades(trades):
                    writehandler.writelines(
                        ['%s,%s,%s,%s,%s,%s,%s,%d,%d,%d,%.2f,%d,%d,%d,%d,%.2f,%.2f\n'
                            % self._enrich_trade(trade) for trade in chunk
                         if DataProcessor._is_trade_valid(trade)]
                    )

            self._get_output_summary()
        except (IOError, InvalidValueError) as e:
            print(e, file=sys.stderr)


def calcTradeStats(input_file_name: str, output_file_name: str) -> None:
    processor = DataProcessor(input_file_name, output_file_name)
    processor.process_data()


def get_args() -> None:
    try:
        parser = argparse.ArgumentParser(description='Enrich trade data from a trade csv file to an output')
        parser.add_argument('--inputFile', help='File containing trades', required=True)
        parser.add_argument('--outputFile', help='File containing enriched trades', required=True)
        args = vars(parser.parse_args())
    except argparse.ArgumentError:
        print('Error: calcStats.py --inputFile=<input file> --outputFile=<output file>', file=sys.stderr)
        sys.exit(2)

    calcTradeStats(args['inputFile'], args['outputFile'])
