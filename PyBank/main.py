#Modules
import os
import csv

#Setting the file path
csvpath = os.path.join("..", "Resources", "budget_data.csv")

#Open the budget data csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

