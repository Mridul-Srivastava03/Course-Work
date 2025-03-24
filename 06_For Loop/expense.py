expenses = [1200, 1300, 1500, 1700]
total_expense = 0

for i in range(len(expenses)):
    expense = expenses[i]
    print(f'Month {i+1}, Expenses = {expense}')
    total_expense += expense

print(f'Total Expenses = {total_expense}')