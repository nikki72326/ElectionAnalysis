# The data we need to retrieve.
import os
import csv

#Assign a variable for the file to load and the path
file_to_load = 'Resources/election_results.csv'
# Create a filename variable to a path to the file to save the analysis data
file_to_save = os.path.join("analysis","election_analysis.txt")

#Open the election results and read the file.
with open(file_to_load) as election_data:

#Read the file object with the reader function.
    file_reader = csv.reader(election_data)
#Print the header row.
    headers = next(file_reader)
    print(headers)

#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candiate won
#4. The total nmber of votes each candiate won
#5. The winner of the election based on popular vote.



#open the file to wire data to it

#write in the file
 
