from financial import *
from calculator import Mortgage


class Analysis(object):
    pass


class FinancialAnalysis(Analysis):
    """
    Facade pattern to consolidates all the CRE financial calculators
    """
    def __init__(self, purchase_price_data, income_data, operating_expenses_data, mortgage_data, units_data):
        self._purchase_price = PurchasePriceDownPayment(**purchase_price_data)
        self._income = Income(**income_data)
        mortgage_data = self._transform_mortgage_data(mortgage_data)
        self._mortgage_calculator = Mortgage(**mortgage_data)
        self._operating_expenses = OperatingExpenses(**operating_expenses_data)
        self._number_of_units = units_data['Number_Of_Units']

    def _transform_mortgage_data(self, mortgage_data):
        mortgage_data = {k.lower():v for k, v in mortgage_data.items()}
        mortgage_data['principal_loan_balance'] = self._purchase_price.principal_loan_balance()
        return  mortgage_data

    def number_of_units(self) -> int:
        return self._number_of_units

    def trailing_rental_income(self) -> float:
        trailing_income = self._income.trailing_rental_income()
        return trailing_income if trailing_income else 0.0

    def annual_gross_rental_income(self) -> float:
        return self._income.gross_rental_income(time_type='y')

    def monthly_gross_rental_income(self) -> float:
        return self._income.gross_rental_income(time_type='m')

    def net_operating_income(self, time_type: str) -> float:
        return self._income.effective_gross_income(time_type) - \
            self._operating_expenses.total_operating_expenses(time_type)

    def mortgage_payment(self, time_type: str) -> float:
        mortgage_payment = self._mortgage_calculator.payment() if time_type == 'm' else \
            self._mortgage_calculator.payment() * 12
        return mortgage_payment

    def cash_flow(self, time_type: str) -> float:
        return self.net_operating_income(time_type) - self.mortgage_payment(time_type)

    def asking_price(self) -> float:
        return self._purchase_price.asking_price()

    def offer_purchase_price(self) -> float:
        return self._purchase_price.offer_purchase_price()

    def market_price(self) -> float:
        return self._purchase_price.offer_purchase_price()

    def renovation_expense(self) -> float:
        return self._purchase_price.renovation_expense()

    def down_payment(self) -> float:
        return self._purchase_price.down_payment()

    def total_cash_required(self) -> float:
        return self._purchase_price.total_cash_required()

    def maintenance_repair_costs(self) -> float:
        return self._operating_expenses.maintenance_repair_costs()

    def property_management_fee(self) -> float:
        return self._operating_expenses.property_management_fee()

    def supplies(self) -> float:
        return self._operating_expenses.supplies()

    def insurance(self) -> float:
        return self._operating_expenses.insurance()

    def operating_expenses(self) -> float:
        return self._operating_expenses.total_operating_expenses(time_type='y')
