import os
import csv

os.chdir(os.path.dirname(os.path.abspath(__file__)))

financial_data = os.path.join('.', 'Resources', 'budget_data.csv')

months = []
profit_loss = []
net_total = 0
avg_change = 0.0

with open(financial_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
#takes each month and profit/loss and append to respective lists
    for row in csvreader:
        months.append(row[0])
        profit_loss.append(int(row[1]))

#calculates total months and net total
total_months = len(months)
net_total = sum(profit_loss)

#calculates average of monthly changes
avg_change_month = []

#finds greatest increase and decrease
greatest_inc = 0
greatest_dec = 0 

for x in range(1, len(profit_loss)):
    profit_change = profit_loss[x] - profit_loss[x - 1]
    avg_change_month.append(profit_change)
    if profit_change > greatest_inc:
        greatest_inc = profit_change
        greatest_inc_month = months[x]
    elif profit_change < greatest_dec:
        greatest_dec = profit_change
        greatest_dec_month = months[x]

avg_change = round(sum(avg_change_month) / len(avg_change_month), 2)

print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${net_total}')
print(f'Average Change: ${avg_change}')
print(f'Greatest Increase in Profits: {greatest_inc_month} (${greatest_inc})')
print(f'Greatest Decrease in Profits: {greatest_dec_month} (${greatest_dec})')
print("----------------------------")

#creates an output textfile
output_file = os.path.join('.', 'Analysis', 'financial_analysis.txt')

with open(output_file, "w") as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("----------------------------\n")
    textfile.write(f'Total Months: {total_months}\n')
    textfile.write(f'Total: ${net_total}\n')
    textfile.write(f'Average Change: ${avg_change}\n')
    textfile.write(f'Greatest Increase in Profits: {greatest_inc_month} (${greatest_inc})\n')
    textfile.write(f'Greatest Decrease in Profits: {greatest_dec_month} (${greatest_dec})\n')
    textfile.write("----------------------------")