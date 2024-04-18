import os
import csv

# Get the current working directory
current_dir = os.path.dirname(__file__)

# Construct the absolute path to the CSV file
filepath = os.path.join(current_dir,'election_data.csv')

# Creating list to store data
election_data = []

# Opening the csv
with open(filepath) as csvfile:
    reader = csv.DictReader(csvfile)
    # Looping through the data to store in a dictionary
    for row in reader:
        election_data.append({"Ballot_ID"})

        # Election results data
total_votes = 369711
candidates = [
    {"name": "Charles Casper Stockham", "votes": 85213},
    {"name": "Diana DeGette", "votes": 272892},
    {"name": "Raymon Anthony Doane", "votes": 11606}
]

# Calculate percentage of votes and find the winner
winner = {"name": "", "percentage": 0, "votes": 0}
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidates:
    percentage = (candidate["votes"] / total_votes) * 100
    print(f"{candidate['name']}: {percentage:.3f}% ({candidate['votes']})")
    if candidate["votes"] > winner["votes"]:
        winner = candidate
print("-------------------------")
print(f"Winner: {winner['name']}")
print("-------------------------")

# Printing the Election Results and exporting to a text file
# Set path for file
output_filepath = os.path.join(current_dir, 'Pypoll_Results.txt')
with open(output_filepath, "w") as text_file:
    print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidates:
    percentage = (candidate["votes"] / total_votes) * 100
    print(f"{candidate['name']}: {percentage:.3f}% ({candidate['votes']})")
    if candidate["votes"] > winner["votes"]:
        winner = candidate
print("-------------------------")
print(f"Winner: {winner['name']}")
print("-------------------------")
