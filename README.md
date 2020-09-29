# python-challenge

PyBank
    -Created a relative path to collect data from the "budget_data" csv
    -Created lists to store data, as the csv reader only reads line by line
    -Created a dictionary to store the dates with their corresponding profit increases/decreases
        -Used this information to determine the greatest profit increase and decrease (using max/min functions)
    -Stored the header row and skipped over it while creating a loop
    -Used the loop to read through total profit/losses, and appended to list in order to both remember the values and sum them up
    -Calculated change from previous profit/losses by storing values in the change_from_previous list, and then making the stored values change along with the csv reader using the loop
    -Calculated average change by using sum of change_from_previous and dividing it by the total count of change_from_previous minus 1 (accounting for the number of changes, which is one less than the count)
    -Printed the analysis into the terminal
    -Created another path in order to write the results in a text file in another folder

PyPoll:
    -Created a relative path to collect data from the "election_data" csv
    -Created lists to store data, as the csv reader only reads line by line
    -Used a loop to count the total number of votes (or entries)
    -Created an if loop to look at candidate names (row 2) and determine whether or not the name was new. If the name was new, it would be recorded (forming a list of candidates)
    -Used a dictionary to store and add one vote for each row the specific candidate name was read in a row
    -Created another for loop to determine the winner as well as calculate percentage of votes
        -Used the total vote count and compared it for each candidates' total vote count to figure out who the winner was
    -Printed analysis to terminal
    -Created a file path so the code could write the analysis into a text file in the designated folder
    