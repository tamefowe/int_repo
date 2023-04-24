"""
    This module will use calculators and rules to
"""
from rule import *
from calculator import *
from reader_writer import InfoReader, InputReader, DBWriter, ExcelWriter
from analysis import FinancialAnalysis
import pandas as pd
from utils import pc, rd
from collections import defaultdict

CALCULATORS = {
    'cap rate': CapRate,
    'cash on cash return': CashOnCashReturn,
    'debt coverage ratio': DebtCoverageRatio,
    'gross rent multiplier': GrossRentMultiplier,
    'occupancy break even point': OccupancyBreakEvenPoint,
}

RULES = [
    OnePercentRule,
    TwoPercentRule,
    SeventyPercentRule,
    UnitExpensesPercentRule,
    UnitMaintenanceRepairsPercentRule,
    UnitPropManagementPercentRule,
    UnitSuppliesPercentRule,
    # UnitTaxesPercentRule,
    UnitInsurancePercentRule,
    RentRollToTrailingPercentRule,
]


class Financials(object):

    def __init__(self, current_analysis, projected_analysis):
        self._financial_values = defaultdict(dict)
        self._financial_analysis = {'current': current_analysis, 'projected': projected_analysis}
        self._compute_financials()

    def _compute_financials_values(self, fin_type):
        annual_gross_rental_income = self._financial_analysis[fin_type].annual_gross_rental_income()
        total_cash_required = self._financial_analysis[fin_type].total_cash_required()
        down_payment = self._financial_analysis[fin_type].down_payment()

        asking_price = self._financial_analysis[fin_type].asking_price()
        market_price = self._financial_analysis[fin_type].market_price()
        offer_purchase_price = self._financial_analysis[fin_type].offer_purchase_price()

        operating_expenses = self._financial_analysis[fin_type].operating_expenses()

        net_operating_income_y = self._financial_analysis[fin_type].net_operating_income(time_type='y')
        net_operating_income_m = self._financial_analysis[fin_type].net_operating_income(time_type='m')

        mortgage_y = self._financial_analysis[fin_type].mortgage_payment(time_type='y')
        mortgage_m = self._financial_analysis[fin_type].mortgage_payment(time_type='m')

        cash_flow_y = self._financial_analysis[fin_type].cash_flow(time_type='y')
        cash_flow_m = self._financial_analysis[fin_type].cash_flow(time_type='m')

        cap_rate = CapRate(net_operating_income_y,
                           asking_price,
                           market_price).cr()
        cash_on_cash_return_renovation = CashOnCashReturn(cash_flow_y,
                                                          down_payment,
                                                          total_cash_required,
                                                          is_renovation=True).cocr()
        cash_on_cash_return_no_renovation = CashOnCashReturn(cash_flow_y,
                                                             down_payment,
                                                             total_cash_required,
                                                             is_renovation=False).cocr()
        debt_coverage_ratio = DebtCoverageRatio(net_operating_income_y, mortgage_y).dcr()
        gross_rent_multiplier = GrossRentMultiplier(offer_purchase_price, annual_gross_rental_income,
                                                    market_price).grm()
        occupancy_break_even_point = OccupancyBreakEvenPoint(operating_expenses, mortgage_y,
                                                             annual_gross_rental_income).obep()
        self._financial_values[fin_type]['db'] = \
            [
                net_operating_income_m,
                net_operating_income_y,
                mortgage_m,
                mortgage_y,
                cash_flow_m,
                cash_flow_y,
                annual_gross_rental_income,
                total_cash_required,
                down_payment,
                cap_rate,
                cash_on_cash_return_renovation,
                cash_on_cash_return_no_renovation,
                debt_coverage_ratio,
                gross_rent_multiplier,
                occupancy_break_even_point,
            ]
        self._financial_values[fin_type]['excel'] = \
            [
                rd(net_operating_income_m),
                rd(net_operating_income_y),
                rd(mortgage_m),
                rd(mortgage_y),
                rd(cash_flow_m),
                rd(cash_flow_y),
                rd(annual_gross_rental_income),
                rd(total_cash_required),
                rd(down_payment),
                pc(cap_rate),
                pc(cash_on_cash_return_renovation),
                pc(cash_on_cash_return_no_renovation),
                rd(debt_coverage_ratio),
                rd(gross_rent_multiplier),
                pc(occupancy_break_even_point),
            ]

    def _compute_financials(self):
        for fin_type in self._financial_analysis.keys():
            self._compute_financials_values(fin_type)

    @staticmethod
    def _columns(type_):
        if isinstance(type_, list):
            return ['Financial'] + [f'Value ({t})' for t in type_]
        return ['Financial', f'Value ({type_})']

    @staticmethod
    def _financials():
        return [
            'Monthly_Net_Operating_Income',
            'Yearly_Net_Operating_Income',
            'Monthly_Mortgage_Payment',
            'Yearly_Mortgage_Payment',
            'Monthly_Cash_Flow',
            'Yearly_Cash_Flow',
            'Annual_Gross_Rental_Income',
            'Total_Cash_Required',
            'Down_Payment',
            'Cap_Rate',
            'Cash_On_Cash_Return_Renovation',
            'Cash_On_Cash_Return_No_Renovation',
            'Debt_Coverage_Ratio',
            'Gross_Rent_Multiplier',
            'Occupancy_Break_Even_Point',
        ]

    def _get_financials_to_excel(self):
        return pd.DataFrame(
            list(
                zip(
                    Financials._financials(),
                    self._financial_values['current']['excel'],
                    self._financial_values['projected']['excel']
                )
            ),
            columns=Financials._columns(['current', 'projected'])
        )

    def _get_financials_to_db(self):
        def get_df(type_):
            return dict(
                zip(
                    Financials._financials(),
                    self._financial_values[type_]['db']
                )
            )

        financial_data = {k: get_df(k) for k in self._financial_values.keys()}
        return financial_data

    def get_financials(self, destination):
        if destination == 'db':
            return self._get_financials_to_db()
        elif destination == 'excel':
            return self._get_financials_to_excel()
        else:
            raise Exception('Incorrect value!')


class Rules(object):

    def __init__(self, current_analysis, projected_analysis):
        self._rule_values = defaultdict(list)
        self._analysis = {'current': current_analysis, 'projected': projected_analysis}
        self._compute_rules()

    def _get_rules_input(self, rule_type: str):
        return {
            'One_Percent_Rule': {
                'monthly_rent': self._analysis[rule_type].monthly_gross_rental_income(),
                'offer_purchase_price': self._analysis[rule_type].offer_purchase_price()
            },
            'Two_Percent_Rule': {
                'monthly_rent': self._analysis[rule_type].monthly_gross_rental_income(),
                'offer_purchase_price': self._analysis[rule_type].offer_purchase_price()
            },
            'Seventy_Percent_Rule': {
                'offer_purchase_price': self._analysis[rule_type].offer_purchase_price(),
                'market_value': self._analysis[rule_type].market_price(),
                'renovation_expense': self._analysis[rule_type].renovation_expense()
            },
            'Expenses_Per_Unit_Rule': {
                'operating_expenses': self._analysis[rule_type].operating_expenses(),
                'number_of_units': self._analysis[rule_type].number_of_units()
            },
            'Maintenance_Repairs_Expenses_Per_Unit_Rule': {
                'maintenance_repair_costs': self._analysis[rule_type].maintenance_repair_costs(),
                'number_of_units': self._analysis[rule_type].number_of_units()
            },
            'Property_Management_Fee_Per_Unit_Rule': {
                'property_management_fee': self._analysis[rule_type].property_management_fee(),
                'total_rental_income': self._analysis[rule_type].annual_gross_rental_income(),
                'number_of_units': self._analysis[rule_type].number_of_units()
            },
            'Maintenance_Supplies_Expenses_Per_Unit_Rule': {
                'supplies': self._analysis[rule_type].supplies(),
                'number_of_units': self._analysis[rule_type].number_of_units()
            },
            'Insurance_Expenses_Per_Unit_Rule': {
                'insurance': self._analysis[rule_type].insurance(),
                'number_of_units': self._analysis[rule_type].number_of_units()
            },
            'Rent_Roll_Vs_Trailing_Percent_Rule': {
                'gross_rental_income': self._analysis[rule_type].annual_gross_rental_income(),
                'trailing_rental_income': self._analysis[rule_type].trailing_rental_income()
            },
        }

    def _compute_rules_values(self, rule_type):
        rules_input = self._get_rules_input(rule_type)
        for cls in RULES:
            args = rules_input[cls.name]
            value = cls(**args).is_met
            self._rule_values[rule_type].append(value)

    def _compute_rules(self):
        for rule_type in self._analysis.keys():
            self._compute_rules_values(rule_type)

    @staticmethod
    def _columns(type_):
        if isinstance(type_, list):
            return ['Financial'] + [f'Value ({t})' for t in type_]
        return ['Financial', f'Value ({type_})']

    @staticmethod
    def _rules():
        return [r.name for r in RULES]

    def _get_rules_to_excel(self):
        return pd.DataFrame(
            list(
                zip(
                    Rules._rules(),
                    self._rule_values['current'],
                    self._rule_values['projected']
                )
            ),
            columns=Rules._columns(['current', 'projected'])
        )

    def _get_rules_to_db(self):
        def get_df(type_):
            return dict(
                zip(
                    Rules._rules(),
                    self._rule_values[type_]
                )
            )

        return {k: get_df(k) for k in self._rule_values.keys()}

    def get_rules(self, destination):
        if destination == 'db':
            return self._get_rules_to_db()
        elif destination == 'excel':
            return self._get_rules_to_excel()
        else:
            raise Exception('Incorrect value!')


class Runner(object):

    def __init__(self, db_server, projection_yrs):
        self._projection_yrs = projection_yrs
        self._property_info = InfoReader().get_data()
        self._financial_input = InputReader().get_data()  # read financials from spreadsheet
        self._financial_analysis = {
            'current_analysis': FinancialAnalysis(**self._financial_input['current']),
            'projected_analysis': FinancialAnalysis(**self._financial_input['projected'])
        }
        self._excel_writer = ExcelWriter()
        # next id = last inserted id in table + 1
        self._current_id = db_server.get_next_id(table_name='Property_Lead')[0][0] - 1
        self._current_id = self._current_id if self._current_id else 1  # default start auto increment value is 1
        self._db_writer = DBWriter(db_server)

    def _get_financial_input(self, destination):
        data = {}
        if destination == 'db':
            data['current'] = {k: v for s in self._financial_input['current'].values() for k, v in s.items()}
            data['projected'] = {k: v for s in self._financial_input['projected'].values() for k, v in s.items()}
            data['current']['idLead'] = self._current_id
            data['current']['Projection_In_Years'] = 0
            data['projected']['idLead'] = self._current_id
            data['projected']['Projection_In_Years'] = self._projection_yrs
        return data

    def _get_financial_output(self, destination):
        fdata = Financials(**self._financial_analysis).get_financials(destination)
        rdata = Rules(**self._financial_analysis).get_rules(destination)
        data = {}

        if destination == 'excel':
            data = fdata.append(rdata, ignore_index=True)

        if destination == 'db':
            data['current'] = fdata['current'] | rdata['current']
            data['current']['idLead'] = self._current_id
            data['current']['Projection_In_Years'] = 0
            data['projected'] = fdata['projected'] | rdata['projected']
            data['projected']['idLead'] = self._current_id
            data['projected']['Projection_In_Years'] = self._projection_yrs
        return data

    def _write_property_info_to_db(self):
        self._db_writer.write({'Property_Lead': self._property_info})

    def _write_financial_input_to_db(self):
        financial_input = self._get_financial_input(destination='db')
        for _, fi in financial_input.items():
            self._db_writer.write({'Property_Financial_inputs': fi})

    def _write_financial_output_to_db(self):
        financial_output = self._get_financial_output(destination='db')
        for _, fi in financial_output.items():
            self._db_writer.write({'Property_Financials': fi})

    def _write_financial_output_to_excel(self):
        financial_output = self._get_financial_output(destination='excel')
        self._excel_writer.write(financial_output)

    def run_fast_fasTER_FASTEST(self, is_save_to_db=False):
        if is_save_to_db:
            self._write_property_info_to_db()
            self._write_financial_input_to_db()
            self._write_financial_output_to_db()
        self._write_financial_output_to_excel()
