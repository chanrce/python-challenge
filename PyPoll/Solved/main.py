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

with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        totalvotes=totalvotes+1
        voterid.append(row[0])
        #candidates.append(row[2])
        if row[2] not in candidatename:
            candidatename.append(row[2])
            candidatedict[row[2]]=0
        candidatedict[row[2]]=candidatedict[row[2]]+1
        #dictionary to store data, created from row reader
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

#printing analysis
PyPollAnalysis= (f"Election Results \n------------------------------------\nTotal Votes: {str(len(voterid))} \n------------------------------------ \nTotal Votes by Candidate: \n{candidatedict} \nPercent of Votes by Candiates: \n{percent_dictionary} \n------------------------------------ \nWinner: {winner}\n------------------------------------ ")
print(PyPollAnalysis)

#exporting analysis to text file

import os

Analysis = os.path.join ("..", "Analysis", "AnalysisPyPoll")

outF = open("../analysis/Analysis", "w")
outF.writelines(PyPollAnalysis)
outF.close()