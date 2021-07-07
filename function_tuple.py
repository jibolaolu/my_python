stock_prices = [('APPL', 300), ('AMZ', 500), ('MSFT', 650)]
print(stock_prices)
for item in stock_prices:
    print(item)

for ticker,prices in stock_prices:
    print(prices + (0.1 * prices))


work_hours = [('Sean', 3000), ('Ayo', 550), ('Tam', 400), ('Jane', 200)]

def employee_check(work_hours):
    max_hours = 0
    emp_of_the_month = ''

    for employee, hours in work_hours:
        if hours > max_hours:
            max_hours = hours
            emp_of_the_month = employee
        else:
            pass

    return emp_of_the_month, max_hours

best_emp = employee_check(work_hours)
print(f'The best employee for the month is {best_emp}')