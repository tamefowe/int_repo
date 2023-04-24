import pandas as pd
import numpy as np


def manipulate(fileName):
    df = pd.read_excel(open(fileName, 'rb'), sheet_name='Sheet1', index_col=0)
    #df = pd.read_csv(fileName, index_col=0)
    df.index = pd.to_datetime(df.index, format='%m/%d/%Y')
    groups = df.groupby([df.ticker, df.index.year, df.index.month])
    results2 = groups.apply(lambda g: g.iloc[-1])
    results = pd.DataFrame()

    for _, group in groups:
        results = results.append(group.iloc[-1])
    print(results)


if __name__ == '__main__':

    fileName = r'C:\Users\Trader\Downloads\q2.xlsx'
    manipulate(fileName)


