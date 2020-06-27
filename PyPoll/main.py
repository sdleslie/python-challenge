# -----------Setup----------
# Modules
import os
import csv

# Set path to Polling Data
pollpath = os.path.join('Resources', 'election_data.csv')

# Open file to read
with open(pollpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

# -----------Main Module----------
# Initialize variabes
votes = 0
Winner_votes = 0
n = 0
# Initialize lists with no elements
Candidate = []
Candidate_votes = []
Percent = []
with open(pollpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
# Read through data
    for row in csvreader:
# Total the votes (one by one)
        votes = votes + 1
# When a new candidate hits the campaign trail add them to our list of candidates and their vote box
        if row[2] not in Candidate:
            Candidate.append(row[2])
            Candidate_votes.append(0)
            Percent.append(0)
            n = n + 1
# When a candidate gets a vote add it to their vote box
        for i in range(n):
            if Candidate[i] == row[2]:
                Candidate_votes[i] = Candidate_votes[i] + 1

# Print Headings
print('-------------------------')
print('Election Results')        
print('-------------------------')

# TotalBlue = chr(27)+"[34m"+ str(votes)
# Trying to learn tesxt coloring anf styles (needs work)

print("Total Votes: " + chr(27)+"[34m" + "\u0332".join(str(votes)))
print(chr(27)+"[30m" + "-------------------------")
# Create a list for each Candidate and the voting stats.  Also the top vote getter is the Winner!
for i in range(n):
    Percent[i] = Candidate_votes[i] / votes
    # Rounding not working as expected, rounds to an integer and roundfloat throes an error
    # NameError: name 'roundfloat' is not defined
    
    if Candidate_votes[i] > Winner_votes:
        Winner_votes = Candidate_votes[i]
        Winner = Candidate[i]
    Votes_by_Candidate = Candidate[i] + ": " + "{:.2%}".format(Percent[i]) + " (" + "{:,}".format(Candidate_votes[i]) + ")"
    # Would like to use percent formatting with decimal formatting
    # Votes_by_Candidate = Candidate[i] + ": " + "{:%}".format(Percent[i]) + " (" + "{:,}".format(Candidate_votes[i]) + ")"
    
    print(Votes_by_Candidate)
#Print Results
print('-------------------------')
WinnerString = 'And the Winner is:' + Winner
if Winner == 'Khan':
    WinnerString = WinnerString + ' (from the Planet SETI Alpha 6)'
print(WinnerString)
print('-------------------------')
# Note: I chose 2 decimal places for the percentage display instead of 3, looks better

# -----------Output Module----------
# Write to text file
output_poll = os.path.join('Resources', 'Election_Results.csv')

# Open and write to the output file
with open(output_poll, 'w') as csvfile:
    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')
    # Write the headers
    csvwriter.writerow(['Candidate', 'Percent of Votes', 'Total Votes'])
    # Write the results
    for i in range(n):
        PercentOutput = round(100 * (Percent[i]),2)
        csvwriter.writerow([Candidate[i], PercentOutput, Candidate_votes[i]])
    # Write the Winner
    csvwriter.writerow([WinnerString])
# Getting an extra line feed for each row!