#PyPoll notes
import os
import csv

#read csv file
PyPoll_Data = os.path.join("./PyPoll_Data.csv")

with open(PyPoll_Data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Read the header row first
    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")

#skip header row

#define variables and lists
    vote_counter = 0
    all_candidates = []
    candidate_vote_totals = {}
    percent_vote = float

    # insert a for loop to count number of rows
    # number of rows will = total number of votes cast
    for row in csvreader:
        vote_counter += 1

    # assign a variable to hold the loop
        candidate_name = row[2]
        if candidate_name not in all_candidates:
            all_candidates.append(candidate_name)
            
            candidate_vote_totals[candidate_name] = 1

        else: 
            candidate_vote_totals[candidate_name] = candidate_vote_totals[candidate_name] + 1

    for candidate_name = row[2]
        if candidate_name not in all_candidates:




    # calculate the percentage of votes by
    # taking vote count total and dividing by
    # the value inside of each dictionary
    #percentage_per_candidate = {k: v / total for total in (sum(a.values()),) for k, v in a.items()}

# Calculate the percentage each candidate received
# Split the dictionary in order to gain 

# Calculate the winner
# https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
# By finding the key that corresponds with highest vote value total
max(candidate_vote_totals, key=lambda key: candidate_vote_totals[key]) 

# Print out the results
print("Election Results")
print("------------------------")
print("Total Votes: " + str(vote_counter))
print(candidate_vote_totals)
print("Winner: " + str(max(candidate_vote_totals, key=lambda key: candidate_vote_totals[key])))