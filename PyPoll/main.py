#Modules
import os
import csv

#Setting the file path
election_data = os.path.join("..", "Resources", "election_data.csv")

with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
