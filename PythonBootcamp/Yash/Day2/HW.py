# Write a program to accept name, empId, basic, special allowances, percentage of bonus and monthly tax saving investments.
# The gross monthly salary is basic + special allowances.
# Compute the annual salary. The gross annual salary also includes the bonus.
# Compute the annual net salary, by deducting taxes as suggested.
# a. Income upto 2.5 lakhs – exempted
# b. Income from 2.5 lakhs to 5 lakhs – 5 %
# c. Income from 5 lakhs to 10 lakhs – 20 %
# d. Income from 10 lakhs onwards – 30 %
# However, if there is any tax saving investment, then there is further exemption of upto 1.5 lakhs annually.
# This would mean that by having tax saving investments of about 1.5 lakhs, an income of 4 lakhs is non-taxable.
# Display the annual gross, annual net and tax payable.


def calculate_tax(annual_income: int, tax_investment: int) -> float:
    
    # Max investment value
    MAX_INVESTMENT = 150000

    if tax_investment >= 150000:
        tax_investment = MAX_INVESTMENT

    taxable_amount = annual_income - tax_investment

    tax_percent = 0

    if (taxable_amount > 1000000):
        tax_percent = 0.3
    elif (taxable_amount > 500000 and taxable_amount <= 1000000):
        tax_percent = 0.2
    elif (taxable_amount > 250000 and taxable_amount <= 500000):
        tax_percent = 0.05

    return taxable_amount * tax_percent


def print_report(employee_name: str, employee_id: int, gross_annual_salary: float, net_annual_salary: float, taxable_amount: float) -> None:
    print("\nTax Report: ")
    print(f"Employee Name: {employee_name}")
    print(f"Employee ID: {employee_id}")
    print(f"Gross Annual Salary: {gross_annual_salary}")
    print(f"Net Annual Salary: {net_annual_salary}")
    print(f"Taxable Amount: {taxable_amount}")


def main():
    
    # Input all Details
    employee_name = str(input("Employee Name: "))
    employee_id = int(input("Employee ID: "))
    basic_salary = int(input("Basic Salary (Monthly): "))
    special_allowance = int(input("Special Allowance (Monthly): "))
    percentage_bonus = int(input("Percentage Bonus: "))
    tax_saving_investment = int(input("Tax Saving Investment (Monthly): "))

    # Annual Income without bonus
    gross_annual_salary = (basic_salary + special_allowance) * 12
    
    # Annual Income with bonus
    gross_annual_salary += gross_annual_salary * (percentage_bonus/100)
    
    yearly_tax_saving_investment = tax_saving_investment * 12

    # Calculate taxed amount
    taxable_amount = calculate_tax(
        gross_annual_salary, yearly_tax_saving_investment)

    net_annual_salary = gross_annual_salary - taxable_amount

    # Print tax report
    print_report(employee_name, employee_id, gross_annual_salary,
                 net_annual_salary, taxable_amount)


main()
