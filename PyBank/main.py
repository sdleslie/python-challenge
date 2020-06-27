# -----------Setup Modules-----------
import os
import csv

# Set path to Budget Data
budgetpath = os.path.join('Resources', 'budget_data.csv')

# Open file to read
with open(budgetpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')


# Checking the calcluation for average change using Excel showed the result
# that is calculated below which is different than the result in the Instructions

# -----------Main Module----------
# Initialize variabes
months = 0
profittotal = 0
profitchange = 0
profitprev = 0
profit = 0
# start = 0
change = 0
sumchange = 0
average = 0
maxchange=0
minchange=0
with open(budgetpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        # Count the rows after the header
        months = 1 + months
        # Total the profit/loss column (1)
        profittotal = float(row[1]) + profittotal
        profitprev = profit
        profit = float(row[1])
        change = profit - profitprev
        if change > maxchange:
            maxchange=change
            maxmonth=row[0]
        elif change <minchange:
            minchange=change
            minmonth=row[0]
        if months == 1:
            change = 0
        sumchange = sumchange + change
averagechange = sumchange/months

print('Financial Analysis')
print('----------------------------')
print('Total Months: ' + str(months))
print('Total: ' + "${:,.0f}".format(profittotal))
print('Average Change: ' + "${:,.2f}".format(averagechange))
print('Greatest Increase in Profits: '+ maxmonth + ' (' "${:,.0f}".format(maxchange)+')')
print('Greatest Decrease in Profits: '+ minmonth + ' (' "${:,.0f}".format(minchange)+')')

# -----------Output Module----------
# Write to text file
output_poll = os.path.join('Resources', 'Financial_Analysis.csv')

# Open and write to the output file
with open(output_poll, 'w',newfile='') as csvfile:
    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')
    # Write a header
    csvwriter.writerow(['Financial Analysis - PyBank'])
    # Write the data
    csvwriter.writerow(['Total Months', months])
    csvwriter.writerow(['Total Volume', profittotal])
    csvwriter.writerow(['Average Change', averagechange])
    csvwriter.writerow(['Greatest Increase in Profits', maxchange])
    csvwriter.writerow(['Greatest Decrease in Profits', minchange])