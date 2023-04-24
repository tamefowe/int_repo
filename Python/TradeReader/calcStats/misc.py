import pandas as pd

from calcStats import calcStats, calcTradeStatsPandas
from bondPricing import bond_yield_to_maturity_discrete
import numpy as np
from pathlib import Path
import struct

PACKET = dict(
    length=dict(offset=0, bytes=2),
    updates=dict(offset=2, bytes=2)
)
UPDATE = dict(
    length=dict(offset=0, bytes=2),
    type=dict(offset=2, bytes=1)
)
TRADE = dict(
    symbol=dict(offset=3, bytes=5),
    trade_size=dict(offset=8, bytes=2),
    trade_price=dict(offset=10, bytes=8),
    dynamic_data=dict(offset=18, bytes=None)
)


class Meas(object):
    def __init__(self, dict_):
        self._offset = dict_.get('offset')
        self._bytes = dict_.get('bytes')
        self._value = None

    def set_value(self, value):
        self._value = value

    @property
    def offset(self):
        return self._offset

    @property
    def bytes(self):
        return self._bytes

    @property
    def value(self):
        return self._value


class Packet(object):
    def __init__(self, packet):
        self._length = Meas(packet.get('length'))
        self._updates = Meas(packet.get('updates'))

    def set_values(self, length, updates):
        self._length.set_value(length)
        self._updates.set_value(updates)

    @property
    def length(self):
        return self._length

    @property
    def updates(self):
        return self._updates


class Update(object):
    def __init__(self, update):
        self._length = Meas(update.get('length'))
        self._type = Meas(update.get('type'))

    def set_values(self, length, type_):
        self._length.set_value(length)
        self._type.set_value(type_)

    @property
    def length(self):
        return self._length

    @property
    def type_(self):
        return self._type


class Trade(object):
    def __init__(self, trade):
        self._symbol = Meas(trade.get('symbol'))
        self._trade_size = Meas(trade.get('trade_size'))
        self._trade_price = Meas(trade.get('trade_price'))
        self._dynamic_data = Meas(trade.get('dynamic_data'))

    def set_values(self, symbol, trade_size, trade_price, dynamic_data):
        self._symbol.set_value(symbol)
        self._trade_size.set_value(trade_size)
        self._trade_price.set_value(trade_price)
        self._dynamic_data.set_value(dynamic_data)

    @property
    def symbol(self):
        return self._symbol

    @property
    def trade_size(self):
        return self._trade_size

    @property
    def trade_price(self):
        return self._trade_price

    @property
    def dynamic_data(self):
        return self._dynamic_data


def run():
    filename = r"C:\cygwin64\home\Trader\C++\iTest\input.dat"

    packet = Packet(PACKET)
    update = Update(UPDATE)
    trade = Trade(TRADE)

    offset = None

    with open(filename, 'rb') as f:
        while True:
            packet_length_bytes = f.read(packet.length.bytes)
            if not packet_length_bytes:
                # eof
                break

            packet_length = int.from_bytes(packet_length_bytes, byteorder='big', signed=False)

            number_packet_updates_bytes = f.read(packet.updates.bytes)
            number_packet_updates = int.from_bytes(number_packet_updates_bytes, byteorder='big', signed=False)

            for u in range(number_packet_updates):
                update_length_bytes = f.read(update.length.bytes)
                update_length = int.from_bytes(update_length_bytes, byteorder='big', signed=False)
                update_type = f.read(update.type_.bytes).decode(encoding='utf-8')

                if update_type == 'T':
                    symbol = f.read(trade.symbol.bytes).decode(encoding='utf-8').strip()
                    trade_size_bytes = f.read(trade.trade_size.bytes)
                    trade_size = int.from_bytes(trade_size_bytes, byteorder='big', signed=False)
                    trade_price_bytes = f.read(trade.trade_price.bytes)
                    trade_price = int.from_bytes(trade_price_bytes, byteorder='big', signed=False) / 10000
                    print("{:d} {:s} @ {:.2f}".format(trade_size, symbol, trade_price))
                    offset = update_length - trade.dynamic_data.offset
                else:
                    offset = update_length - 3

                f.seek(offset)

            print()

def power(n, m):
    if m == 0:
        return 1
    return power(n, m - 1) * n


def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return sum_of_digits(int(n / 10)) + int(n % 10)


def greatest_common_divisor(n, m):
    if m == 0:
        return m
    return greatest_common_divisor(m, n % m)


def decimal_to_binary(n):
    if n == 0:
        return 0
    return n % 2 + 10 * decimal_to_binary(int(n / 2))


def findPairs(n, t):
    d = {}
    result = []
    for a in n:
        d[t - a] = a
    for a in n:
        if a in d and a != d[a] and (d[a], a) not in result and (a, d[a]) not in result:
            result.append((a, d[a]))
    return result

def read_binary(ifilename, ofilename):
    with open(ifilename, 'rb') as f:
        binary_data = f.read()


def solution(A):
    # write your code in Python 3.6
    sum_of_elements = 0
    len_of_array = len(A)
    number_of_fragments = 0
    map_of_sum_of_elements = {}

    if not A:
        return 0

    for index in range(len_of_array):

        sum_of_elements += A[index]

        if sum_of_elements == 0:
            number_of_fragments += 1

        indexes_of_fragments = []

        if sum_of_elements in map_of_sum_of_elements:

            indexes_of_fragments = map_of_sum_of_elements.get(sum_of_elements)
            for i in range(len(indexes_of_fragments)):
                number_of_fragments += 1

        indexes_of_fragments.append(index)
        map_of_sum_of_elements[sum_of_elements] = indexes_of_fragments

        if number_of_fragments > 1000000000:
            return -1

    return sum_of_elements


def all_perms(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]


def solution_(N, S, T):
    ships = S.split(',')
    ships = [s.split() for s in ships]
    ships = [[i[0][:-1], i[1][:-1], i[0][-1], i[1][-1]] for i in ships]
    ships = [[int(i[0]), int(i[1]), ord(i[2].lower()) - 96, ord(i[3].lower()) - 96] for i in ships]

    attacks = T.split()
    attacks = [[int(a[0]), ord(a[1].lower()) - 96] for a in attacks]

    sunks = 0
    hits = 0

    attack_cords = [attack for attack in attacks]
    for ship in ships:
        ships_cords = []
        for x in range(ship[0], ship[1] + 1):
            for y in range(ship[2], ship[3] + 1):
                ships_cords.append([x, y])

        ishits = [a for a in attack_cords if a in ships_cords]

        if len(ishits) == len(ships_cords):
            sunks += 1
            continue

        if len(ishits) > 0:
            hits += 1

    return "%d,%d" % (sunks, hits)


def get_col_number_from_name(col_name, LETTERS='ABCD'):
    """ Convert given  Excel-style cell name to column number"""
    multiplier = 1
    col_number = 0
    for char in col_name[::-1]:
        cn = LETTERS.find(char) + 1
        col_number += (multiplier * cn)
        multiplier *= 4
    return col_number


def get_number_of_cells(pattern):
    import re
    letter_num = []
    digit_num = []
    for pattern in pattern.split(':'):
        letter_num.append(re.search('[A-Z]+', pattern).group(0))
        digit_num.append(re.search('\d+', pattern).group(0))

    lnum = get_col_number_from_name(letter_num[1]) - get_col_number_from_name(letter_num[0]) + 1
    dnum = int(digit_num[1]) - int(digit_num[0]) + 1

    if lnum < 0 or dnum < 0:
        return -1

    num = lnum * dnum

    return num


def find_unique_dirs(paths):
    uniq_dirs = {}
    for path in paths:
        if path[0] == '/':
            if not uniq_dirs:
                uniq_dirs = {'/'}
            dirs = path.split('/')
            dirs = dirs[1:-1]
            current_dir = ''
            for dir in dirs:
                current_dir = '{}/{}'.format(current_dir, dir)
                uniq_dirs.add(current_dir)

    return uniq_dirs


def cumulative_loss(returns):
    df = pd.DataFrame(returns)
    df = df.cumsum()
    ret_pcts = df.pct_change()
    cumul_rets = (ret_pcts + 1).cumprod() - 1

    return cumul_rets



def main():
    # n = 22661
    # print(sum_of_digits(n))
    # n, m = 2, 3
    # print(power(n, m))
    # arr =[1, 2, 3, 2,3, 4 , 5,6]
    # t = 6
    # print(findPairs(arr, t))
    # ifilename = "/home/Trader/C++/iTest/input.dat"
    # ofilename = "/home/Trader/C++/iTest/output.txt"
    # read_binary(ifilename, ofilename)
    input_file = r'C:\Users\Trader\PycharmProjects\TradeReader\trades.csv'
    # output_file1 = r'C:\Users\Trader\PycharmProjects\TradeReader\enrichedTrades_no_pandas.csv'
    output_file2 = r'C:\Users\Trader\PycharmProjects\TradeReader\enrichedTrades._yes_pandas.csv'

    # calcTradeStats.calc_trade_stats(input_file, output_file1)
    # calcTradeStatsPandas.calc_trade_stats(input_file, output_file2)

    # x = solution_(4, '1B 2C,2D 4D', '2B 2D 3D 4D 4A')

    # y =  solution_(12, '1A 2A,12A 12A', '12A')

    c = np.array([10, 10, 10, 10, 10, 10, 10, 110])
    n = len(c) + 1
    t = np.arange(1, n)
    r = .09
    # b = np.sum(c * (1. / np.power((1 + r), t)))
    # x = bond_yield_to_maturity_discrete(t, c, b)

    # pattern = 'A1:C2'
    pattern = 'C11:AA21'
    # n = get_number_of_cells(pattern)

    paths = ['/a/b/', '/x/y']
    uq = find_unique_dirs(paths)
    print()
