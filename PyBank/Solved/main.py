#Modules
import os
import csv

#Setting the file path
budget_data = os.path.join("..", "Resources", "budget_data.csv")

#Lists to store data
months = []


profitinc = []
profitdec = []
change_from_previous = []

#dictionary to store dates with corresponding changes
changedict = {}

#make variables
totalprofitlosses = 0
previous = 0


#Open the budget data 
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    for row in csvreader:
        months.append(row[0])
        totalprofitlosses += int(row[1])

        change = int(row[1]) - previous
        change_from_previous.append(change)
        previous = int(row[1])
        

candidatedict = dict(zip(months, change_from_previous))
#max(candidatedict(change_from_previous))

Keymax = max(candidatedict, key=candidatedict.get) 
print("max is: " + str(Keymax) + ":" + str(max(change_from_previous)))

    
#calculation of average change
avgchange = sum(change_from_previous[1:])/(len(change_from_previous)-1)
        
#counting number of months
print(str(len(months)))

#printing results
print(totalprofitlosses)
print(avgchange)


#for range month in months 
#if max(change_from_previous):
#    print(month)
#print(min(change_from_previous))

#cleaned_csv = zip(title,price,subscribers,reviews,review_percent,length)
#output_file = os.path.join("web_final.csv")

#BELOW CONVERT TO TXT FILE!!!!!!!!!!!!!
#with open(output_file, "w") as datafile:
    #writer = csv.writer(datafile)
    #writer.writerow(["Title", "Course Price", "Subscribers,"Reviews Left", "Percent of Review", ])