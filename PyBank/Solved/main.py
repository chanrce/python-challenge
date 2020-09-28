#Modules
import os
import csv

#Setting the file path
budget_data = os.path.join("..", "Resources", "budget_data.csv")

#Lists to store data
months = []
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
        
changesdict = dict(zip(months, change_from_previous))

#determining max change and corresponding month/year
profitchangesmax = max(changesdict, key=changesdict.get) 
profitchangesmin = min(changesdict, key=changesdict.get) 


#calculation of average change
avgchange = sum(change_from_previous[1:])/(len(change_from_previous)-1)
        

#printing financial analysis

analysis= (f"Financial Analysis \n------------------------------------\nTotal Months: {str(len(months))} \nTotal: ${totalprofitlosses} \nAverage Change: ${avgchange} \nGreatest Increase in Profits: {profitchangesmax}: {max(change_from_previous)} \nGreatest Decrease in Profits: {profitchangesmin}: {min(change_from_previous)}")

#printing analysis in terminal
print(analysis)
#print("Financial Analysis")
#print("------------------------------------")
#print("Total Months: " + str(len(months)))
#print("Total: " + str(totalprofitlosses))
#print("Average Change: " + str(avgchange))
#print("Greatest Increase in Profits: " + str(profitchangesmax) + ":" + str(max(change_from_previous)))
#print("Greatest Decrease in Profits: " + str(profitchangesmin) + ":" + str(min(change_from_previous)))



#outF = open("myOutFile.txt", "w")
#outF.writelines(all_lines)
#outF.close()

#cleaned_csv = zip(title,price,subscribers,reviews,review_percent,length)
#output_file = os.path.join("web_final.csv")

#BELOW CONVERT TO TXT FILE!!!!!!!!!!!!!
#with open(output_file, "w") as datafile:
    #writer = csv.writer(datafile)
    #writer.writerow(["Title", "Course Price", "Subscribers,"Reviews Left", "Percent of Review", ])