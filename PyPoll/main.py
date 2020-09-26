#Modules
import os
import csv

#Setting the file path
election_data = os.path.join("..", "Resources", "election_data.csv")

#Lists to store data
voterid = []


#candidates =[]

with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    for row in csvreader:
        voterid.append(row[0])
        #candidates.append(row[2])

        #dictionary to store data, created from row reader
        candidatedict = {"county": row[1], "candidate": row[2]}



#prints total number of votes cast
print(str(len(voterid)))