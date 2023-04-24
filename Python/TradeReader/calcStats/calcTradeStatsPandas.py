import pandas as pd


class DataProcessor(object):

    def __init__(self, input_file, output_file):
        self._input_file = input_file
        self._output_file = output_file
        self._trades = None

    def _read_raw_trades(self):
        self._trades = pd.read_csv(self._input_file, index_col=[0])
        self._trades.index = pd.to_datetime(self._trades.index, format='%H:%M:%S.%f')
        self._trades.index = self._trades.index.time
        print()


    def _write_enriched_trades(self):
        self._trades.to_csv(self._output_file)

    def __remove_nans(self):
        # find total number of NaNs
        # trades.isna().sum()
        # Symbol          0
        # EventType       0
        # Side            1
        # FillSize        1
        # FillPrice       1
        # FillExchange    1
        # dtype: int64

        # show rows of NaNs
        # trades[trades.isna().any(axis=1)]
        #                    Symbol EventType Side  FillSize  FillPrice FillExchange
        # LocalTime
        # 1900-01-01 12:00:00   LNCH      TIME  NaN       NaN        NaN          NaN

        # drop all rows with NaNs
        self._trades = self._trades.dropna()

        # fill NaN with 0's
        #self._trades = self._trades.fillna(0)

        # values = {col1: 0, col2: 2, ...}
        # self._trades = self._trades.fillna(value=values)

    def __remove_other_invalid_trades(self):
        # find all invalid data
        # trades[trades.EventType != 'TRADE']
        #                    Symbol EventType Side  FillSize  FillPrice FillExchange
        # LocalTime
        # 1900-01-01 11:11:11   RUFR      NIMN    b   -1111.0        0.0       NASDAQ

        # trades[~trades.Side.isin(['b','t','s'])]
        # Empty DataFrame
        # Columns: [Symbol, EventType, Side, FillSize, FillPrice, FillExchange]
        # Index: []

        # trades.FillExchange.unique()
        # array(['NYSE', 'NASDAQ'], dtype=object)

        # remove invalid data
        self._trades = self._trades[self._trades.EventType == 'TRADE']

    def __fix_data_types(self):
        # check correct data types and change accordingly
        #trades.dtypes

        # LocalTime               object
        # Symbol                  object
        # EventType               object
        # Side                    object
        # FillSize               float64
        # FillPrice              float64
        # FillExchange            object
        self._trades = self._trades.astype({'FillSize': 'int32'})
        #self._trades.FillSize = self._trades.FillSize.astype(int)

    def _clean_trades(self):
        # clean data
        self.__remove_nans()
        self.__remove_other_invalid_trades()
        self.__fix_data_types()

    def _enrich_trades(self):
        # Calculate results
        self._trades['SizeBought'] = self._trades.apply(lambda r: r['FillSize'] if r['Side'] == 'b' else 0, axis=1)
            #np.vectorize(lambda x, y: y if x == 'b' else 0)(self._trades.Side, self._trades.FillSize)
        self._trades['SizeSold'] = self._trades.apply(lambda r: r['FillSize'] if r['Side'] in ['s', 't'] else 0, axis=1)
            #np.vectorize(lambda x, y: y if x in ['s', 't'] else 0)(self._trades.Side, self._trades.FillSize)

        self._trades['PriceBought'] = self._trades.apply(lambda r: r['FillPrice'] if r['Side'] == 'b' else 0.0, axis=1)
            #np.vectorize(lambda x, y: y if x == 'b' else 0.0)(self._trades.Side, self._trades.FillPrice)
        self._trades['PriceSold'] = self._trades.apply(lambda r: r['FillPrice'] if r['Side'] in ['s', 't'] else 0.0, axis=1)
            #np.vectorize(lambda x, y: y if x in ['s', 't'] else 0.0)(self._trades.Side, self._trades.FillPrice)

        self._trades['SymbolBought'] = self._trades.groupby('Symbol')['SizeBought'].cumsum()
        self._trades['SymbolSold'] = self._trades.groupby('Symbol')['SizeSold'].cumsum()

        self._trades['SymbolPosition'] = self._trades['SymbolBought'] - self._trades['SymbolSold']

        self._trades['SymbolNotional'] = self._trades.FillPrice * self._trades.FillSize

        self._trades['ExchangeBought'] = self._trades.groupby('FillExchange')['SizeBought'].cumsum()
        self._trades['ExchangeSold'] = self._trades.groupby('FillExchange')['SizeSold'].cumsum()

        self._trades['TotalBought'] = self._trades['SizeBought'].cumsum()
        self._trades['TotalSold'] = self._trades['SizeSold'].cumsum()

        self._trades['TotalBoughtNotional'] = (self._trades.PriceBought * self._trades.SizeBought).cumsum()
        self._trades['TotalSoldNotional'] = (self._trades.PriceSold * self._trades.SizeSold).cumsum()

        self._trades = self._trades.drop(columns=['SizeBought', 'SizeSold', 'PriceBought', 'PriceSold'])

    def _get_summary_statistics(self):
        exchange_sizes = ''
        for ex in sorted(self._trades.FillExchange.unique()):
            ex_bought = "%s %s: %s\n" % (ex, 'Bought', '{:,d}'.format(
                self._trades.loc[self._trades.FillExchange == ex, 'ExchangeBought'].iloc[-1]))
            ex_sold = "%s %s: %s\n" % (ex, 'Sold', '{:,d}'.format(
                self._trades.loc[self._trades.FillExchange == ex, 'ExchangeSold'].iloc[-1]))
            exchange_sizes += (ex_bought + ex_sold)

        most_active_symbols = self._trades.groupby('Symbol')['FillSize'].sum().sort_values(ascending=False)[:10]
        most_active_symbols_str = ', '.join(
            ['%s(%s)' % (sym, '{:,d}'.format(size)) for sym, size in most_active_symbols.items()])

        args = [
            '{:,d}'.format(len(self._trades)),
            '{:,d}'.format(self._trades.TotalBought.iloc[-1]),
            '{:,d}'.format(self._trades.TotalSold.iloc[-1]),
            '{:,d}'.format(self._trades.FillSize.sum()),
            '${:0,.2f}'.format(self._trades.TotalBoughtNotional.iloc[-1]),
            '${:0,.2f}'.format(self._trades.TotalSoldNotional.iloc[-1]),
            exchange_sizes,
            '{:,d}'.format(int(self._trades.FillSize.mean())),
            '{:,d}'.format(int(self._trades.FillSize.median())),
            most_active_symbols_str
        ]
        summary = """
WITH PANDAS
-------------

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

10 Most Active Symbols: %s""" % (tuple(args))
        print(summary)

    def process_data(self):
        self._read_raw_trades()
        self._clean_trades()
        self._enrich_trades()
        self._write_enriched_trades()
        self._get_summary_statistics()


def calcTradeStats(input_file, output_file):
    dp = DataProcessor(input_file, output_file)
    dp.process_data()


