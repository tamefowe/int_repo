#
# Know
# deal under market?
# can rent be increased?
# possible creating financing?
#
# 4 things to become an expert in your market
# 1. price/unit (price/ square foot if commercial space)
# 2. cap rate for the market
# 3. market rents (for 1-2-3 bedroom apt units)
# 4. expenses/unit (for B and C-class apts)
#

import abc


class Rule(abc.ABC):
    name = 'NAME'
    is_met = False
    threshold = 0
    interpretation = 'INTERPRETATION'

    @abc.abstractmethod
    def calculate(self):
        pass


class OnePercentRule(Rule):
    name = 'One_Percent_Rule'
    threshold = .01
    interpretation = 'its monthly rent must be equal to or no less than 1% of the purchase price.'

    def __init__(self, monthly_rent=0.0, offer_purchase_price=0.0):
        self._monthly_rent = monthly_rent
        self._offer_purchase_price = offer_purchase_price
        self.calculate()

    def calculate(self):
        self.is_met = self._monthly_rent >= self.threshold * self._offer_purchase_price


class TwoPercentRule(OnePercentRule):
    name = 'Two_Percent_Rule'
    threshold = .02
    interpretation = 'its monthly rent must be equal to or no less than 2% of the purchase price.'


class SeventyPercentRule(Rule):
    name = 'Seventy_Percent_Rule'
    threshold = .7
    interpretation = 'paying no more than 70% of a property’s after-repair value (ARV) minus the cost of the repairs'

    def __init__(self, offer_purchase_price=0.0, market_value=0.0, renovation_expense=0.0):
        self._offer_purchase_price = offer_purchase_price
        self._after_repair_value = market_value + renovation_expense
        self.calculate()

    def calculate(self):
        self.is_met = self._offer_purchase_price <= self.threshold * self._after_repair_value


class UnitExpensesPercentRule(Rule):
    name = 'Expenses_Per_Unit_Rule'
    threshold = (5000, 6000)
    interpretation = 'operating expenses should not be > $5K/6K/unit)'

    def __init__(self, number_of_units, operating_expenses=0.0):
        self._operating_expenses_unit = operating_expenses / number_of_units
        self.calculate()

    def calculate(self):
        self.is_met = self.threshold[0] <= self._operating_expenses_unit <= self.threshold[1]


class UnitMaintenanceRepairsPercentRule(Rule):
    name = 'Maintenance_Repairs_Expenses_Per_Unit_Rule'
    threshold = (650, 750)
    interpretation = 'maintenance repairs should not be > $605/750/unit)'

    def __init__(self, number_of_units, maintenance_repair_costs=0.0):
        self._maintenance_repair_costs_unit = maintenance_repair_costs / number_of_units
        self.calculate()

    def calculate(self):
        self.is_met = self.threshold[0] <= self._maintenance_repair_costs_unit <= self.threshold[1]
        print()


class UnitPropManagementPercentRule(Rule):
    name = 'Property_Management_Fee_Per_Unit_Rule'
    threshold = (.04, .10)
    interpretation = 'property management fee should not be > .04 to .1 / unit)'

    def __init__(self, number_of_units, property_management_fee=0.0, total_rental_income=0.0):
        self._property_management_fee_unit = property_management_fee / number_of_units
        self._total_rental_income = total_rental_income
        self.calculate()

    def calculate(self):
        cash_collected = (self.threshold[0] * self._total_rental_income,
                          self.threshold[1] * self._total_rental_income)
        self.is_met = cash_collected[0] <= self._property_management_fee_unit <= cash_collected[1]


class UnitSuppliesPercentRule(Rule):
    name = 'Maintenance_Supplies_Expenses_Per_Unit_Rule'
    threshold = (100, 200)
    interpretation = 'maintenance supplies should not be > $100/200/unit)'

    def __init__(self, number_of_units, supplies=0.0):
        self._supplies_unit = supplies / number_of_units
        self.calculate()

    def calculate(self):
        self.is_met = self.threshold[0] <= self._supplies_unit <= self.threshold[1]

    def outcome(self):
        if not self.is_met and self._supplies_unit > self.threshold[1]:
            return f"{self._supplies_unit} > {self.threshold}"
        return "passed"


class UnitTaxesPercentRule(Rule):
    name = 'Taxes_Expenses_Per_Unit_Rule'
    interpretation = """call the county tax accessor and ask how to calculate taxes multi familial properties
                        don't give address otherwise it will trigger  a publicly tax assessment report"""

    def calculate(self):
        pass


class UnitInsurancePercentRule(Rule):
    name = 'Insurance_Expenses_Per_Unit_Rule'
    threshold = (450, 550)
    interpretation = 'insurance should not be > $450/550/unit)'

    def __init__(self, number_of_units, insurance=0.0):
        self._insurance_unit = insurance / number_of_units
        self.calculate()

    def calculate(self):
        self.is_met = self.threshold[0] <= self._insurance_unit <= self.threshold[1]


class RentRollToTrailingPercentRule(Rule):
    name = 'Rent_Roll_Vs_Trailing_Percent_Rule'
    threshold = .01
    interpretation = '12-month trailing rent roll total should not be > 10% of actual rent roll'

    def __init__(self, gross_rental_income=0.0, trailing_rental_income=0.0):
        self._gross_rental_income = gross_rental_income
        self._trailing_rental_income = trailing_rental_income
        self.calculate()

    def calculate(self):
        self.is_met = self._gross_rental_income >= self.threshold * self._trailing_rental_income


class UnitToExpensePercentRule(Rule):
    name = 'Unit_To_Expense_Percent_Rule'
    threshold = {
        (0, 4): .25,
        (5, 20): (.30, .35),
        (20, 50): (.35, .45),
        (50, 100): (.45, .55)
    }

    def __init__(self, number_of_units=0, effective_gross_income=0.0):
        self._number_of_units = number_of_units
        self._effective_gross_income = effective_gross_income
        self._operating_expenses = 0.0

    def calculate(self):
        percent = 0
        for tpl_unit, tpl_percent in self.threshold.items():
            if (self._number_of_units - tpl_unit[0]) < (tpl_unit[1] - self._number_of_units):
                percent = tpl_percent[0]
            elif (self._number_of_units - tpl_unit[0]) == (tpl_unit[1] - self._number_of_units):
                percent = sum(tpl_percent) // 2
            else:
                percent = tpl_percent[1]
        self._operating_expenses = self._effective_gross_income * percent

    def operating_expenses(self) -> float:
        self.calculate()
        return self._operating_expenses
