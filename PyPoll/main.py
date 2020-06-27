import os
import csv

os.chdir(os.path.dirname(os.path.abspath(__file__)))

election_data = os.path.join('.', 'Resources', 'election_data.csv')

counter = {}

with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvreader)

#creates a dictionary counting votes for each candidate. idea for for loop taken from Udacity Intro to Python course
    for row in csvreader:
        counter[row[2]] = counter.get(row[2], 0) + 1

#adds all the values in the dictionary to calculate total votes
    total_votes = sum(counter.values())

#finds the candidate with the most number of votes and saves the key
    winner = max(counter, key=counter.get)

    #prints out all results
    print("Election Results")
    print("----------------------------")
    print(f'Total Votes: {total_votes}')
    print("----------------------------")
    for key, value in counter.items():
        print(f'{key}: {round((value/total_votes) * 100, 2)}% ({value})')
    print("----------------------------")
    print(f'Winner: {winner}')
    print("----------------------------")

#create an output file
output_file = os.path.join('.', 'Analysis', 'vote_counting.txt')

with open(output_file, "w") as textfile:
    textfile.write("Election Results\n")
    textfile.write("----------------------------\n")
    textfile.write(f'Total Votes: {total_votes}\n')
    textfile.write("----------------------------\n")
    for key, value in counter.items():
        textfile.write(f'{key}: {round((value/total_votes) * 100, 2)}% ({value})\n')
    textfile.write("----------------------------\n")
    textfile.write(f'Winner: {winner}\n')
    textfile.write("----------------------------")