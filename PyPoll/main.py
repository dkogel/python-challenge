import os
import csv




#read in the csv (skip header)
input_path= os.path.join("Resources/election_data.csv")

all_candidates= []
unique_candidates= []

khan_count= 0
correy_count= 0
li_count= 0
otooley_count= 0


with open(input_path) as csvfile:
    csvreader= csv.reader(csvfile, delimiter= ",")
    header=next(csvreader)
    
    #list the unique candidates
    for row in csvreader:
        if row[2] not in unique_candidates:
            unique_candidates.append(row[2])
        #count the votes each unique candidate received with a for loop
        #Khan, Correy, Li, O'Tooley

        if row[2] == "Khan":
            khan_count= khan_count + 1
        elif row[2] == "Correy":
            correy_count= correy_count + 1
        elif row[2] == "Li":
            li_count= li_count + 1
        elif row[2] == "O'Tooley":
            otooley_count= otooley_count +1
    print(unique_candidates)
    print(khan_count)
    print(correy_count)
    print(li_count)
    print(otooley_count)

#calculate the percentage of votes each candidate received
total_votes= khan_count + correy_count + li_count + otooley_count
khan_percent= khan_count/total_votes
correy_percent= correy_count/total_votes
li_percent= li_count/total_votes
otooley_percent= otooley_count/total_votes
print(khan_percent)
print(correy_percent)
print(li_percent)
print(otooley_percent)

#calculate the winner with max()
candidate_dict={khan_count:"Khan",correy_count:"Correy",
                li_count:"Li",otooley_count:"O'Tooley"}

max= max(khan_count,correy_count,li_count,otooley_count)
print(f"{candidate_dict[max]}")

#output data to terminal

#output the data to csv

