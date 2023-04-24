#include <iostream>
using namespace std;

struct Picture {
};
struct Address {
    string address;
    string city;
    string state;
    string zip_code;
};


class PropertyInformation {
    Address address;
    Picture picture;
};

struct PropertyDescription {
    int bedrooms;
    int bathrooms;
    int square_foot;
    string  year_built;
    string description;
};
class Purchase {
    double purchase_price;
    double purchase_closing_costs;
    bool is_rehabbing;
};
        After Repair Value (ARV)
A property’s ARV is its market value after all rehab work has been completed.
Repair costs
The total amount it will cost to renovate the property. Include labor, materials, etc.
Paint
        Roofing
flooring
        lanscaping
electrical
        concrete
gutters/facia
        Septic
foundation
        decks
cabinets
        demolition
plumbing
        carpentry
windows
        doows
HVAC
        permits
custom

        annual property value growth (appreciation 2%)
How much do you expect the value of the property to increase per year?
For example, if the property is worth $100,000 today and you think next year
        it will be worth $103,000, enter 3%. Be sure to use a conservative number that
accounts for both the ups and downs in the market.
Loan Details
Is Cash purchase
        Is not Cash purchase
Loan amount x% of purchase price and y% down payment (x+y=100)
interest rate (%)
point charged
Often when you take out a loan, you will pay "points" (aka: fees) on the loan.
One point is equal to 1% of the loan amount. For example, a $100,000 loan with
2 points would be $2,000. Note: this is most common with hard money lenders.
loan term (years)
Rental Income
Gross monthly income (how much rental can I charge)
rent
        laundry Service
        water reimbursement
        custom
Annual income growth
        How much do you expect the rental income to rise each year? For example,
if the property will rent for $1,000 today and you think next year it will
        rent for $1,020, enter 2%. Be sure to use a conservative number that accounts
for both the ups and downs in the market.
Expenses
        property taxes
        annual/monthly
        insurance
annual/monthly

        Maintenance, vacancy, capital expenditures, and management fees are expressed
as percentages of gross monthly income.

Repair & maintenance
All properties require ongoing maintenance when things break (and with tenants - they will).
This number is usually expressed as a percentage of the rent. Although repairs will depend
on numerous factors such as the location and age of the property; typical repair costs tend
to be between 5-15% of the gross monthly rent.
Vacancy
        Vacancy rate is the cost of the property sitting empty due to tenant turnover.
This number can vary depending on the area, so consult with a local property manager or
landlord as to the local norms. Typical vacancy rates are between 3%-10% of
        the gross monthly rent, but again, that can depend on the area.
Capital Expenditures
CapEx, short for Capital Expenditures, are the large less-than-frequent improvements done to
a property such as roofs, parking lots, siding, or appliances. CapEx will depend on numerous
        factors such as property type, the location of the property, and the age of the property.
Management Fees
How much does a local property manager charge to manage the property each month? This number
is usually expressed as a percentage. This rate may differ based on location and property type,
but typical rates hover between 7-12% of the Gross Monthly Rent.
Electricity
        Gas
Water & sewer
HOA Fees
Garbage
        Other
Annual expenses growth (2%)
Expenses tend to go up, but by how much? In this field, enter a percentage you think inflation
will cause your expenses to rise over time.
int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
