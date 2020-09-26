#Modules
import os
import csv

#Setting the file path
election_data = os.path.join("..", "Resources", "election_data.csv")

#Lists to store data
voterid = []

with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    for row in csvreader:
        voterid.append(row[0])


print(str(len(voterid)))