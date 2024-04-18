import os
import csv

# Get the current working directory
current_dir = os.path.dirname(__file__)

# Construct the absolute path to the CSV file
filepath = os.path.join(current_dir,'budget_data.csv')

# Creating list to store data
budget_data = []

# Opening the CSV
with open(filepath) as csvfile:
    reader = csv.DictReader(csvfile)
    # Looping through the data to store in a dictionary
    for row in reader:
        budget_data.append({"month": row["Date"], "amount": int(row["Profit/Losses"]), "change": 0})

# Calculating the total months
total_months = len(budget_data)

# Looping through the dictionary in order to calculate changes between months
previous_amount = budget_data[0]["amount"]
for i in range(1, total_months):
    budget_data[i]["change"] = budget_data[i]["amount"] - previous_amount
    previous_amount = budget_data[i]["amount"]

# Calculating the total amount
total_amount = sum(row['amount'] for row in budget_data)

# Calculating the average of amount changes
total_change = sum(row['change'] for row in budget_data[1:])  # exclude the first month's change
average = round(total_change / (total_months - 1), 2)

# Getting the Greatest Increase and Decrease from the changes
get_increase = max(budget_data, key=lambda x: x['change'])
get_decrease = min(budget_data, key=lambda x: x['change'])

# Printing the Final Analysis
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${total_amount}')
print(f'Average Change: ${average}')
print(f'Greatest Increase in Profits: {get_increase["month"]} (${get_increase["change"]})')
print(f'Greatest Decrease in Profits: {get_decrease["month"]} (${get_decrease["change"]})')

# Printing the Final analysis and exporting to a text file
# Set path for file
output_filepath = os.path.join(current_dir, 'PyBank_Results.txt')
with open(output_filepath, "w") as text_file:
    print('Financial Analysis', file=text_file)
    print('----------------------------', file=text_file)
    print(f'Total Months: {total_months}', file=text_file)
    print(f'Total: ${total_amount}', file=text_file)
    print(f'Average Change: ${average}', file=text_file)
    print(f'Greatest Increase in Profits: {get_increase["month"]} (${get_increase["change"]})', file=text_file)
    print(f'Greatest Decrease in Profits: {get_decrease["month"]} (${get_decrease["change"]})', file=text_file)