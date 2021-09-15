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

#greatest increase and decrease
min(profit_changes)
max(profit_changes)

print("")
print("Financial Analysis")
print("---------------------------")
print(f"Total months: {total_months}")
print(f"Total: {total_profit}")
print(f"Average Change: {average_changes}")
print(f"Greatest Decrease in profits: {min(profit_changes)}")
print(f"Geatest Increase in profits: {max(profit_changes)}")

#write to text file
output_path= os.path.join("Analysis/Financial_Analysis.txt")

with open(output_path, "w") as txtfile:
    txtfile.write("")
    txtfile.write("Financial Analysis \n")
    txtfile.write(" \n")
    txtfile.write("-------------------------- \n")
    txtfile.write(" \n")
    txtfile.write(f"Total months: {total_months} \n")
    txtfile.write(f"Total: {total_profit} \n")
    txtfile.write(f"Average Change: {average_changes} \n")
    txtfile.write(f"Greatest Decrease in profits: {min(profit_changes)} \n")
    txtfile.write(f"Greatest Increase in profits: {max(profit_changes)} \n")
