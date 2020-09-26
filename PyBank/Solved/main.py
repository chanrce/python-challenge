#Modules
import os
import csv

#Setting the file path
budget_data = os.path.join("..", "Resources", "budget_data.csv")

#Lists to store data
months = []
profitlosses = []

#sumchanges = []
profitinc = []
profitdec = []
change_from_previous = []

#make variables
totalprofitlosses = 0
previous = 0


#Open the budget data 
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    for row in csvreader:
        months.append(row[0])
        profitlosses.append(row[1])
        totalprofitlosses += int(row[1])

        change = int(row[1]) - previous
        change_from_previous.append(change)
        previous = int(row[1])
    
    avgchange = sum(change_from_previous[1:])/(len(change_from_previous)-1)

        #changes = (int[profitlosses(row[1])]-int([profitlosses(next(row[1]))))
        #changes = round(int(row[1])-int(next(row[1]))
        #sumchanges += int(changes)

       # subscribers.append(row[5])
        #reviews.append(row[6])

        #percent = round(int(row[6])/int(row[5]),2)
        #review_percent.append(percent)

        #new_length = row[9].split(" ")
        #length.append(float(new_length[0]))

#counting number of months
print(str(len(months)))
print(totalprofitlosses)
print(avgchange)


#adding up the profits/losses




#cleaned_csv = zip(title,price,subscribers,reviews,review_percent,length)
#output_file = os.path.join("web_final.csv")

#BELOW CONVERT TO TXT FILE!!!!!!!!!!!!!
#with open(output_file, "w") as datafile:
    #writer = csv.writer(datafile)
    #writer.writerow(["Title", "Course Price", "Subscribers,"Reviews Left", "Percent of Review", ])