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
        if row[2] == "Khan":
            khan_count= khan_count + 1
        elif row[2] == "Correy":
            correy_count= correy_count + 1
        elif row[2] == "Li":
            li_count= li_count + 1
        elif row[2] == "O'Tooley":
            otooley_count= otooley_count +1

#calculate the percentage of votes each candidate received
total_votes= khan_count + correy_count + li_count + otooley_count
khan_percent= khan_count/total_votes
correy_percent= correy_count/total_votes
li_percent= li_count/total_votes
otooley_percent= otooley_count/total_votes


#calculate the winner with max()
candidate_dict={khan_count:"Khan",correy_count:"Correy",
                li_count:"Li",otooley_count:"O'Tooley"}

max= max(khan_count,correy_count,li_count,otooley_count)


#output data to terminal

print("")
print("Election Results ")
print("--------------------------- ")
print(f"Total Votes: {total_votes}")
print("--------------------------- ")
print(f"Khan: {round(khan_percent*100,3)}%  ({khan_count})")
print(f"Correy: {round(correy_percent*100,3)}% ({correy_count})")
print(f"Li: {round(li_percent*100,3)}% ({li_count})")
print(f"O'Tooley: {round(otooley_percent*100,3)}% ({otooley_count})")
print("--------------------------- ")
print(f"Winner: {candidate_dict[max]}")
print("--------------------------- ")

#output the data to csv
output_path= os.path.join("Analysis/election_results.txt")

with open(output_path, "w") as txtfile:

    txtfile.write(" \n")
    txtfile.write("Election Results \n")
    txtfile.write("---------------------- \n")
    txtfile.write(f"Total Votes: {total_votes} \n")
    txtfile.write("---------------------- \n")
    txtfile.write(f"Khan: {round(khan_percent*100,3)}% ({khan_count}) \n")
    txtfile.write(f"Correy: {round(correy_percent*100,3)}% ({correy_count}) \n")
    txtfile.write(f"Li: {round(li_percent*100,3)}% ({li_count}) \n")
    txtfile.write(f"O'Tooley: {round(otooley_count*100,3)}% ({otooley_count}) \n")
    txtfile.write("---------------------- \n")
    txtfile.write(f"Winner: {candidate_dict[max]} \n")
    txtfile.write("---------------------- \n")

