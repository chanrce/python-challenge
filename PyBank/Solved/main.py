#Modules
import os
import csv

#Setting the file path
budget_data = os.path.join("..", "Resources", "budget_data.csv")

#Open the budget data 
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

