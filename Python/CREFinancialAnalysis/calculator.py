from config import DEFAULT_CONFIG
import numpy as np


class Calculator(object):
    name = 'name'
    threshold = 'threshold'
    interpretation = 'interpretation'
    value = 0.0

    def calculate(self):
        pass


class Mortgage(Calculator):
    name = 'mortgage payment'

    def __init__(self, principal_loan_balance=0.0,
                 amortization_schedule=DEFAULT_CONFIG['amortization schedule'],
                 interest_rate=DEFAULT_CONFIG['interest rate']):
        self._principal_loan_balance = principal_loan_balance
        self._amortization_schedule = amortization_schedule if amortization_schedule \
            else DEFAULT_CONFIG['amortization schedule']
        self._interest_rate = interest_rate if interest_rate else DEFAULT_CONFIG['interest rate']
        self.calculate()

    def calculate(self):
        self._interest_rate /= 12
        self._amortization_schedule *= 12
        numerator = self._principal_loan_balance * self._interest_rate
        denominator = 1 - (1 + self._interest_rate) ** (-self._amortization_schedule)
        self.value = numerator / denominator

    def payment(self):
        return self.value


class CapRate(Calculator):
    name = 'Capitalization Rate'
    threshold = '4% to 5% - Brooklyn/Queens'
    interpretation = """compare property values and measurer an investment profitability
                        mount of money investor can expect to earn per year as a %"""

    def __init__(self, net_operating_income=0.0, asking_price=0.0, market_price=0.0):
        self._net_operating_income = net_operating_income
        self._asking_price = asking_price
        self._market_price = market_price
        self.calculate()

    def calculate(self):
        property_value = self._asking_price if self._asking_price is not None else self._market_price
        self.value = self._net_operating_income / property_value

    def cr(self):
        return self.value


class CashOnCashReturn(Calculator):
    name = 'Cash on cash return with or w/o renovations'
    threshold = '8%'
    interpretation = """measures the annual return the investor made on the property in relation to 
                        the amount of mortgage paid during the same year.
                        quick way to determine whether purchasing an investment property is worth it"""

    def __init__(self, annual_cash_flow=0.0, down_payment=0.0, total_cash_required=0.0, is_renovation=0.0):
        self._annual_cash_flow = annual_cash_flow
        self._down_payment = down_payment
        self._total_cash_required = total_cash_required
        self._is_renovation = is_renovation
        self.calculate()

    def calculate(self):
        if not self._is_renovation and self._down_payment:
            self.value = self._annual_cash_flow / self._down_payment

        if self._is_renovation and self._total_cash_required:
            self.value = self._annual_cash_flow / self._total_cash_required

    def cocr(self):
        return self.value


class DebtCoverageRatio(Calculator):
    name = 'Debt Coverage Ratio'
    threshold = '> 1 or 1.2 minimum'
    interpretation = 'assess an entity ability to generate enough cash to cover its debt service obligations'

    def __init__(self, net_operating_income=0.0, annual_mortgage_payment=0.0):
        self._net_operating_income = net_operating_income
        self._annual_mortgage_payment = annual_mortgage_payment
        self.calculate()

    def calculate(self):
        self.value = self._net_operating_income / self._annual_mortgage_payment

    def dcr(self):
        return self.value


class GrossRentMultiplier(Calculator):
    name = 'Gross Rent Multiplier'
    threshold = '6 to 10'
    interpretation = 'the number of years the property would take to pay for itself in gross received rent'

    def __init__(self, offer_purchase_price=0.0, annual_gross_rental_income=0.0, market_price=0.0):
        self._offer_purchase_price = offer_purchase_price
        self._annual_gross_rental_income = annual_gross_rental_income
        self._market_price = market_price
        self.calculate()

    def calculate(self):
        if self._offer_purchase_price:
            self.value = self._offer_purchase_price / self._annual_gross_rental_income
        else:
            self.value = self._market_price / self._annual_gross_rental_income

    def grm(self):
        return self.value


class OccupancyBreakEvenPoint(Calculator):
    name = 'Occupancy Break Even Point'
    threshold = ''
    interpretation = 'occupancy income is equal to my mortgage payment'

    def __init__(self, operating_expenses=0.0, annual_mortgage_payment=0.0, annual_gross_rental_income=0.0):
        self._operating_expenses = operating_expenses
        self._annual_mortgage_payment = annual_mortgage_payment
        self._annual_gross_rental_income = annual_gross_rental_income
        self.calculate()

    def calculate(self):
        self.value = (self._operating_expenses + self._annual_mortgage_payment) / self._annual_gross_rental_income

    def obep(self):
        return self.value


class IRR(Calculator):
    name = 'Internal Rate of Return'
    definition = 'Discount rate that makes the Present Value of Cash ZERO'
    use = 'Compare investments amongst various industries'
    interpretation = 'IRR > Required Rate of Return (RRR)'

    def __init__(self, list_of_cashflows):
        self._list_of_cashflows = list_of_cashflows
        self.calculate()

    def calculate(self):
        self.value = round(np.irr(self._list_of_cashflows), 3)

    def irr(self):
        return self.value * 100
