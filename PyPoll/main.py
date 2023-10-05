import os
import csv

# define
voterid = []
candidates = []
filtered_cand = []
candidate_votes = 0
winner_votes = 0
winner_name = ""
candidate_name = []

csvpath = os.path.join('Resources','election_data.csv')
outpath = os.path.join('Analysis', 'pypoll_output.txt')

# read in election_data.csv and initiate output file
with open(outpath, 'w') as outfile:
    outfile.write("PyPoll Election Results\n-------------------------\n")

    with open(csvpath, encoding='UTF-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        csv_header = next(csvfile)

        for row in csvreader:
            # make list of all voter IDs to count ballots cast
            voterid.append(row[0])
            # complete list of candidates
            candidates.append(row[2])
        
        outfile.write(f'Total votes cast: {len(voterid)}\n' '-------------------------\n')
        print(f'Total votes cast: {len(voterid)}')

    # first sort alphabetically
    # append first candidate to list
    # run through each candidate in the list and add to filtered list
    # print filtered list
        candidates.sort()  
        filtered_cand.append(candidates[0])
        for i in range(0,int(len(candidates))-1):
            if candidates[i] != candidates[i+1]:
                filtered_cand.append(candidates[i+1])
        print(filtered_cand)

            # percent votes won
            # total votes won
        for fc in filtered_cand:
            for candi in candidates:
                if fc == candi:
                    candidate_votes += 1
            outfile.write(f"{fc}: {int(candidate_votes)/int(len(voterid)):.3%}, ({candidate_votes})\n")
            print(f"{fc}: {int(candidate_votes)/int(len(voterid)):.3%}, ({candidate_votes})")
          
            # Winner
            if candidate_votes > winner_votes:
                winner_votes = candidate_votes
                winner_name = fc
            candidate_votes = 0
        print(f'Winner: {winner_name}')
    outfile.write('-------------------------\n'f'Winner: {winner_name}')

        
