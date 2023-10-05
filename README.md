## PythonChallenge

# PyBank 

read in & skip header using code from cereal.py, class 3, 01-Evr_CerealCleaner

calculations:
1. use '.append' to add all dates (the first column in the dataset) to a new list, similar to the census.py example, and count the total number of items using len()
2. total profits/losses calculated using the logic from the StarCounter example, we start with a variable ('total') equal to 0, and then add the value of row 1 as an integer.
   this would add profits and subtract losses.
4. to find the changes we want a new list with just the profits (or losses) again using the .append method
   the total change would be equal to the last value in the list minus the first, and to find the average we divide this by 85.
6. loop through the list of profit/losses, making a new list containing the difference between the profit one month and the profit the month before.
   from this new list we can use the max/min method from https://www.w3schools.com/python/ref_func_max.asp

PyPoll

read in csv same as PyBank

calculations:
1. total votes cast would be the len() of a list of all voter ids
2. complete list of candidates using the same .append method, and then outside of the "for row in csv reader loop", loop through candidate list and add to new list if the candidate at x+1 is not equal to candidate at position x
3. nested loops to find total and percent votes won
	first loop through the filtered candidate list and then the full candidate list, adding to a variable each time the value in filtered candidate list equals the value in full candidate list. 
	using f string to print number of votes per candidate and calculate percentages
4. the winner can be found using an if statement inside the filtered candidate loop, setting variable winner_votes as equal to candidate_votes when it is greater than that before it, so at the end winner_votes equals the greatest number of votes in the dataset

I used nested 'with' loops to print all outputs to a new file, 'outfile' with the command outfile.write(). This code came from the 09-Ins_Reading_Writing_CSV section of class.

Other sources:
I attended a tutoring session to talk through the nested 'with' loops and the structure of the README, along with other small clarifying questions. The links below I used to see the documentation for some commands and methods, or to find which arguments a function accepted. 
- https://docs.python.org/3/tutorial/datastructures.html
- https://stackoverflow.com/questions/74557297/f-string-with-percent-and-fixed-decimals
- https://www.w3schools.com/python/ref_func_print.asp
- https://stackoverflow.com/questions/2918362/writing-string-to-a-file-on-a-new-line-every-time
