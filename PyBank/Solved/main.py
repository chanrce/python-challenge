#Modules
import os
import csv

#Setting the file path
budget_data = os.path.join("..", "Resources", "budget_data.csv")

#Lists to store data
months = []
profitlosses = []
avgchanges = []
profitinc = []
profitdec = []


#Open the budget data 
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:
        title.append(row[1])
        price.append(row[4])
        subscribers.append(row[5])
        reviews.append(row[6])

        percent = round(int(row[6])/int(row[5]),2)
        review_percent.append(percent)

        new_length = row[9].split(" ")
        length.append(float(new_length[0]))

cleaned_csv = zip(title,price,subscribers,reviews,review_percent,length)
output_file = os.path.join("web_final.csv")

#BELOW CONVERT TO TXT FILE!!!!!!!!!!!!!
#with open(output_file, "w") as datafile:
    #writer = csv.writer(datafile)
    #writer.writerow(["Title", "Course Price", "Subscribers,"Reviews Left", "Percent of Review", ])