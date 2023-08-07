import csv

def analyze_election_data(csv_file):
    with open(csv_file, newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        
        total_votes = 0
        candidates = {}
        
        for row in csv_reader:
            total_votes += 1
            candidate_name = row['Candidate']
            
            if candidate_name not in candidates:
                candidates[candidate_name] = 0
            candidates[candidate_name] += 1
        
        candidate_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidates.items()}
        winner = max(candidates, key=candidates.get)
        
        return total_votes, candidates.keys(), candidate_percentages, candidates, winner

csv_file_path = 'election_data.csv'
total_votes, candidate_names, candidate_percentages, candidate_votes, winner = analyze_election_data(csv_file_path)

print("Election Result")

print("___________________________________")
print("Total votes cast:", total_votes)
print("____________________________________")

for candidate, percentage in candidate_percentages.items():
    print(f"{candidate}: {percentage:.2f}%   (Total Votes: {candidate_votes[candidate]})")

print("------The Winner-------")

print("Winner of the election:", winner)

print("------End Report----------")
