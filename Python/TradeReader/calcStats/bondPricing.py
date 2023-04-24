import numpy as np
import pandas as pd

def bonds_price_discrete(times, cashflows, r):
    p = 0

    for i in range(len(times)):
        p += cashflows[i] / np.power((1+r), times[i])

    return p


def bond_yield_to_maturity_discrete(times, cashflows, bondprice):

    ACCURACY = 1e-5
    MAX_ITERATIONS = 200
    bot = 0
    top = 1.

    while bonds_price_discrete(times, cashflows, top) > bondprice:
        top *= 2

    r = .5 * (top + bot)

    for _ in range(MAX_ITERATIONS):

        diff = bonds_price_discrete(times, cashflows, r) - bondprice

        if np.abs(diff) < ACCURACY:
            return r

        if diff > 0:
            bot = r

        else:
            top = r

        r = .5 * (top + bot)

    return r


def bonds_duration_discrete(times, cashflows, r):
    b = 0
    d = 0

    for i in range(len(times)):
        d += times[i] * cashflows[i] / np.power((1 + r), times[i])
        b += cashflows[i] / np.power((1 + r), times[i])

    return d / b


# Code 4.4: Calculating the Macaulay duration of a bond

def bonds_duration_macaulay_discrete(times, cashflows, bondprice):
    y = bond_yield_to_maturity_discrete(times, cashflows, bondprice)

    return bonds_duration_discrete(times, cashflows, y)  # use YTM in duration calculation


# Code 4.5: Modified duration
def bonds_duration_modifed_discrete(times, cashflows, bond_price):
    y = bond_yield_to_maturity_discrete(times, cashflows, bond_price)
    d = bonds_duration_discrete(times, cashflows, y)

    return d / (1 + y)


# Code 4.6: Bond convexity with a flat term structure and annual compounding

def bonds_convexity_discrete(times, cashflows, r):
    cx = 0.

    for i in range(len(times)):
        cx += cashflows[i] * times[i] * (times[i] + 1) / np.power((1 + r), times[i])

    b = bonds_price_discrete(times, cashflows, r)

    return (cx / (np.power((1 + r), 2))) / b


# Code 4.7: Bond price calculation with continously compounded interest and a flat term structure
def bonds_price(cashflows_times, cashflows, r):
    p = 0

    for i in range(len(cashflows_times)):
        p += np.exp(-r * cashflows_times[i]) * cashflows[i]

    return p


# Code 4.8: Bond duration calculation with continously compounded interest and a flat term strucutre
def bonds_duration(cashflows_times, cashflows, r):
    s = 0
    d1 = 0

    for i in range(len(cashflows_times)):
        s += cashflows[i] * np.exp(-r * cashflows_times[i])
        d1 += cashflows_times[i] * cashflows[i] * np.exp(-r * cashflows_times[i])

    return d1 / s


# Code 4.9: Calculating the Macaulay duration of a bond with continously
# compounded interest and a flat term structure
def bonds_duration_macaulay(cashflows_times, cashflows, bond_price):
    y = bond_yield_to_maturity_discrete(cashflows_times, cashflows, bond_price)

    return bonds_duration(cashflows_times, cashflows, y)  # use YTM in duration


# Code 4.10: Bond convexity calculation with continously compounded interest
# and a flat term structure
def bonds_convexity(times, cashflows, r):
    c = 0
    for i in range(len(times)):
        c += cashflows[i] * np.power(times[i], 2) * np.exp(-r * times[i])

    b = bonds_price(times, cashflows, r)

    return c / b

def calc_bond_price():
    pass


def garch_model(fileName):
    df = pd.read_csv(r'C:\Users\Trader\Downloads\PTON.csv', index_col=0)
    df.index = pd.to_datetime(df.index, format='%Y-%m-%d')
    df = df.rename(columns={'Adj Close': 'Adjclose'})

    average = df.Adjclose.mean()
    standard_deviation = df.Adjclose.std()
    variance = df.Adjclose.var()

    Constant_mu = average
    unconditional_variance_omega = variance
    ARCH_alpha = 0.0
    GARCH_beta = 0.0
    alpha_beta = ARCH_alpha + GARCH_beta
    Long_run_volatility = np.sqrt(Constant_mu / (1 - ARCH_alpha - GARCH_beta))

    df['Return'] = df.Adjclose.pct_change()
    df['Residual'] = df.Return - df.Adjclose.mean()
    df['Squared_Residual'] = np.square(df.Residual)
    df['Lagged_Squared_Residual'] = df.Squared_Residual.shift(1)
