#import modules
import os
import csv

# set path for file
csvpath= os.path.join("Resources/budget_data.csv")

all_months= []
all_profit= []
profit_changes= []

lastrow= 0

# open with CSV
with open(csvpath) as csvfile:

    csvreader= csv.reader(csvfile, delimiter=",")

    #skip header row
    csv_header= next(csvfile)

    for row in csvreader:
        #add all months to total_months list
        all_months.append(row[0])
        total_months=len(all_months)

        #add up net profits
        all_profit.append(int(row[1]))
        total_profit= sum(all_profit)

        #create changes list
        change= int(row[1])-lastrow
        profit_changes.append(change)
        lastrow= int(row[1])
        
        
#remove first element from changes list because it's not a change
profit_changes.pop(0)

#calculate average change
num_changes= len(profit_changes)
sum_changes= sum(profit_changes)
average_changes= round(sum_changes/num_changes,2)


print(total_months)
print(total_profit)
print(average_changes)