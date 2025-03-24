expenses = [1200, 1900, 2100, 1700, 2300]

for i, expense in enumerate(expenses):
    if expense > 2000:
        print(f'Month {i+1} has expenses above 2000')
        break