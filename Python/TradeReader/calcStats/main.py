import pandas as pd
import numpy as np
#from calcStats import calcStats


trainingdata = pd.read_csv('C:\\Users\\Trader\\Downloads\\stocktrainingdata.csv', header=0)


def run():
    input_file = r'C:\Users\Trader\PycharmProjects\TradeReader\trades.csv'
    # output_file1 = r'C:\Users\Trader\PycharmProjects\TradeReader\enrichedTrades_no_pandas.csv'
    output_file = r'C:\Users\Trader\PycharmProjects\TradeReader\enrichedTrades._yes_pandas.csv'

   # calcStats.calcTradeStats(input_file, output_file)


import matplotlib.pyplot as plt
trainingdata = pd.read_csv('C:\\Users\\Trader\\Downloads\\stocktrainingdata.csv', header=0)
trainingdata['Stock price'] = trainingdata['Stock price'].str.replace('$','')
trainingdata['Stock price'] = pd.to_numeric(trainingdata['Stock price'], errors='coerce')
trainingdata['Transitory Earnings per share'] = pd.to_numeric(trainingdata['Transitory Earnings per share'], errors='coerce')
trainingdata['Earnings per share'] = pd.to_numeric(trainingdata['Earnings per share'], errors='coerce')
trainingdata = trainingdata.dropna()
plt.plot(trainingdata['Stock price'],trainingdata['Earnings per share'])
import math

def averageScores():
    # Each record of table1 contains the ID (unique for each student) and grade for a student; 
    # Each record of table2 contains the Name, ID, Gender, and Age for a student.
    # Output: a list of two integers
    table1 = [[1, 70], [2, 75], [7, 90], [4, 85], [5, 100], [6, 60]]
    table2 = [["ab", 1, "m", 9], ["ac", 2, "f", 9], ["bc", 7, "f", 11], ["bd", 4, "f", 8], ["be", 5, "m", 9], ["bf", 6, "m", 7], ["bg", 9, "m", 8]]
    # Write your code here
    tab1 = pd.DataFrame(table1, columns=['ID', 'Grade'])
    tab2 = pd.DataFrame(table2, columns=['Name', 'ID', 'Gender', 'Age'])
    tab = pd.merge(tab1, tab2, how='right')
    tab = tab[tab.Age < 10].groupby('Gender')['Grade'].mean()
    tab = tab.apply(lambda x: math.trunc(x))
    x = tab.tolist()
    print(tab.tolist())


def computeRank(arr):
    # Write your code here
    sorted_arr = sorted(arr, reverse=True)
    print(sorted_arr)
    for i, a in enumerate(sorted_arr):

        print(f"{i+1}")
    return


if __name__ == "__main__":
    arr = [4,1,3,1,4]
    print(f"{computeRank(arr)}")


