# The data we need to retrieve.
import csv
import os

#Assign a variable for the file to load and the path
file_to_load = 'Resources/election_results.csv'

# Create filename variables to a paths to the file the analysis data
file_to_save = os.path.join ("analysis","election_analysis.txt")

#initialize the total vote counter
total_votes = 0

#declare a new list
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage=0

#Open the election results and read the file.
with open (file_to_load) as election_data:
    file_reader = csv.reader(election_data)

#Read the header row.
    headers = next(file_reader)

#capture the candidate name and total votes for each row
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]

    #stop repeat of candidate names  
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

        #start tracking the vote count for each candidate
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

#save the results to a text file.
with open(file_to_save, "w") as txt_file: 
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n") 
    print(election_results, end="")

    txt_file.write(election_results) 

#Get the percentage of votes, print in terminal and save to file
    for candidate_name in candidate_votes:
        votes = candidate_votes [candidate_name]
        vote_percentage = float(votes) /float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        print(candidate_results)       
        txt_file.write(candidate_results)

#Determine winning counts
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
   
    winning_candidate_summary = (
        f"------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"  
        f"------------------------\n")  
    print(winning_candidate_summary)
   
    txt_file.write(winning_candidate_summary)