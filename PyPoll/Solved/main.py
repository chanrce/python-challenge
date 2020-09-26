#Modules
import os
import csv

#Setting the file path
election_data = os.path.join("..", "Resources", "election_data.csv")

#Lists to store data
voterid = []
candidatename =[]

candidatedict = {}

totalvotes = 0
#candidates =[]

with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    for row in csvreader:
        totalvotes=totalvotes+1
        voterid.append(row[0])
        #candidates.append(row[2])
        if row[2] not in candidatename:
            candidatename.append(row[2])
            candidatedict[row[2]]=0
        candidatedict[row[2]]=candidatedict[row[2]]+1
        #dictionary to store data, created from row reader
        #candidatedict = {"county": row[1], "candidate": row[2]}
    percent_dictionary = {}
    maximumvotes = 0
    winner = ""

    #runs a for loop on percent dict, runs through candidate's votes in dict to determine winner
    for x in candidatedict:
        percent_dictionary[x]=round((candidatedict[x]/totalvotes)*100)
        votes = candidatedict.get(x)
        if votes > maximumvotes:
            maximumvotes = votes
            winner = x


#prints total number of votes cast
print(str(len(voterid)))
print(candidatename)
print(candidatedict)
print(percent_dictionary)
print(winner)