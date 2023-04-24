from config import DEFAULT_CONFIG


class Financial(object):
    pass

class PurchasePriceDownPayment(Financial):

    def __init__(self, Asking_Price,
                 Offer_Purchase_Price,
                 Renovation_Expense=0.0,
                 Down_Payment_Amount=0.0,
                 Down_Payment_Percent=DEFAULT_CONFIG['down payment percent']):
        self._asking_price = Asking_Price
        self._offer_purchase_price = Asking_Price if not Offer_Purchase_Price else Offer_Purchase_Price
        self._renovation_expense = Renovation_Expense
        self._down_payment_amount = Down_Payment_Amount
        self._down_payment_percent = Down_Payment_Percent
        self._get_down_payment_amount()

    def _get_down_payment_amount(self):
        self._down_payment_amount = self._offer_purchase_price * DEFAULT_CONFIG['down payment percent'] \
                                        if not self._down_payment_percent else self._down_payment_amount

    def asking_price(self):
        return self._asking_price

    def renovation_expense(self):
        return self._renovation_expense

    def offer_purchase_price(self):
        return self._offer_purchase_price

    def down_payment(self):
        return self._down_payment_amount

    def principal_loan_balance(self):
        return self._offer_purchase_price - self._down_payment_amount

    def total_cash_required(self):
        return self._down_payment_amount + self._renovation_expense


class Income(Financial):

    def __init__(self,
                 Income_Time_Type,
                 Gross_Rental_Income,  # all income from rental only - do not include fee, laundry unit, etc.
                 Vacancy=0.0,  # credit loss in % of rents
                 Non_Revenue_Units=0.0,
                 # units occupied but that do not produce rent - occupied by owner, property manager or maintenance
                 # personnel, etc.
                 Bad_Debt=0.0,  # unrecoverable delinquent income
                 Concessions=0.0,  # incentives given to tenants in order  to boost / stabilize occupancy
                 Other_Income=0.0,
                 # not related to rental areas such as late fees, application fees, laundry units, etc.
                 Rubs_Cam_Income=0.0,
                 # Residential Utilities Billing system / common area maintenance - amount reimbursed to property
                 # owner for services expenditures such as utility, maintenance, paving, common area expenses
                 Vacancy_Rate=DEFAULT_CONFIG['vacancy rate'],
                 **kwargs
                 ):
        self._time_type = Income_Time_Type
        self._gross_rental_income = Gross_Rental_Income
        self._vacancy = Vacancy
        self._non_revenue_units = Non_Revenue_Units
        self._bad_debt = Bad_Debt
        self._concessions = Concessions
        self._other_income = Other_Income
        self._rubs_cam_income = Rubs_Cam_Income
        self._vacancy_rate = Vacancy_Rate
        self._get_vacancy()
        self._total_rental_income = self._calculate_total_rental_income()
        self._effective_gross_income = self._calculate_effective_gross_income()
        self._monthly_rental_income_trailing_12_month = sum(kwargs.values())

    def _get_vacancy(self):
        self._vacancy = self._gross_rental_income * self._vacancy_rate if self._vacancy_rate else self._vacancy

    def _calculate_total_rental_income(self) -> float:
        return self._gross_rental_income - self._vacancy - self._non_revenue_units - self._bad_debt - self._concessions

    def _calculate_effective_gross_income(self) -> float:
        return self._total_rental_income + self._other_income + self._rubs_cam_income

    def trailing_rental_income(self):
        return self._monthly_rental_income_trailing_12_month

    def gross_rental_income(self, time_type: str) -> float:
        if self._time_type == 'm':
            return self._gross_rental_income if time_type == 'm' else self._gross_rental_income * 12
        else:
            return self._gross_rental_income if time_type == 'y' else self._gross_rental_income / 12

    def total_rental_income(self, time_type: str) -> float:
        if self._time_type == 'm':
            return self._total_rental_income if time_type == 'm' else self._total_rental_income * 12
        else:
            return self._total_rental_income if time_type == 'y' else self._total_rental_income / 12

    def effective_gross_income(self, time_type: str) -> float:
        if self._time_type == 'm':
            return self._effective_gross_income if time_type == 'm' else self._effective_gross_income * 12
        else:
            return self._effective_gross_income if time_type == 'y' else self._effective_gross_income / 12


class OperatingExpenses(Financial):

    def __init__(self,
                 Expense_Time_Type,
                 # Administrative
                 Accounting=0.0,
                 Advertising=0.0,
                 Legal=0.0,
                 Marketing=0.0,
                 Office_Supplies=0.0,
                 Administrative_Other=0.0,
                 # Repair & Maintenance
                 Janitorial=0.0,
                 Landscaping=0.0,
                 Maintenance_Repair_Costs=0.0,
                 Maintenance_Repair_Salary=0.0,
                 Pool=0.0,
                 Supplies=0.0,
                 # Utilities
                 Cable=0.0,
                 Electric=0.0,
                 Gas_Oil=0.0,
                 Sewer_Water=0.0,
                 Telephone=0.0,
                 Trash=0.0,
                 Utilities_Other=0.0,
                 # Miscellaneous
                 Miscellaneous=0.0,
                 # Fixed Expenses
                 Taxes=0.0,
                 Fire_Liability_Insurance=0.0,
                 Insurance_Other=0.0,
                 Property_Management_Fee=0.0,
                 Property_Management_Salary=0.0,
                 Capital_Reserve=0.0):
        self._time_type = Expense_Time_Type
        # Administrative
        self._accounting = Accounting
        self._advertising = Advertising
        self._legal = Legal
        self._marketing = Marketing
        self._office_supplies = Office_Supplies
        self._administrative_other = Administrative_Other
        # Repair & Maintenance
        self._janitorial = Janitorial
        self._landscaping = Landscaping
        self._maintenance_repair_costs = Maintenance_Repair_Costs
        self._maintenance_repair_salary = Maintenance_Repair_Salary
        self._pool = Pool
        self._supplies = Supplies
        # Utilities
        self._cable = Cable
        self._electric = Electric
        self._gas_oil = Gas_Oil
        self._sewer_water = Sewer_Water
        self._telephone = Telephone
        self._trash = Trash
        self._utilities_other = Utilities_Other
        # Miscellaneous
        self._miscellaneous = Miscellaneous
        # Fixed Expenses
        self._taxes = Taxes
        self._fire_liability_insurance = Fire_Liability_Insurance
        self._insurance_other = Insurance_Other
        self._property_management_fee = Property_Management_Fee
        self._property_management_salary = Property_Management_Salary
        self._capital_reserve = Capital_Reserve
        self._total_operating_expenses = self._calculate_total_operating_expenses()

    def _administrative(self) -> float:
        return sum([self._accounting, self._advertising, self._legal, self._marketing, self._office_supplies,
                    self._administrative_other])

    def _repair_maintenance(self) -> float:
        return sum([self._janitorial, self._landscaping, self._maintenance_repair_costs,
                    self._maintenance_repair_salary, self._pool, self._supplies])

    def _utilities(self) -> float:
        return sum([self._cable, self._electric, self._gas_oil, self._sewer_water, self._telephone, self._trash,
                    self._utilities_other])

    def _total_variable_expenses(self) -> float:
        return self._administrative() + self._repair_maintenance() + self._utilities() + self._miscellaneous

    def _insurance(self) -> float:
        return self._fire_liability_insurance + self._insurance_other

    def _property_management(self) -> float:
        return self._property_management_fee + self._property_management_salary

    def _total_fixed_expenses(self) -> float:
        return self._taxes + self._insurance() + self._property_management()

    def _calculate_total_operating_expenses(self) -> float:
        return sum([self._total_variable_expenses(), self._total_fixed_expenses(), self._capital_reserve])

    def maintenance_repair_costs(self) -> float:
        return self._maintenance_repair_costs

    def supplies(self) -> float:
        return self._supplies

    def property_management_fee(self) -> float:
        return self._property_management_fee + self._property_management_salary

    def insurance(self) -> float:
        return self._insurance_other + self._fire_liability_insurance

    def total_operating_expenses(self, time_type: str) -> float:
        if self._time_type == 'm':
            return self._total_operating_expenses if time_type == 'm' else self._total_operating_expenses * 12
        else:
            return self._total_operating_expenses if time_type == 'y' else self._total_operating_expenses / 12
