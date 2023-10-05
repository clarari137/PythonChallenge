import os
import csv

# define
total = 0
months = []
profits = []
incdec = []

csvpath = os.path.join('Resources','budget_data.csv')
outpath = os.path.join('Analysis', 'pybank_output.txt')

# read in budget__data.csv, initialize output file, skip header
with open(outpath, 'w') as outfile:
    outfile.write("PyBank Financial analysis\n ---------------------------------------\n")

    with open(csvpath, encoding='UTF-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        csv_header = next(csvfile)

        for row in csvreader:
            # total number of months by appending all dates (months) in the dataset to months list
            months.append(row[0])
            #total profits/losses over the period by adding all values in the second column
            total += int(row[1])
            #changes in profits/losses by creating new list containing the dollar values
            profits.append(int(row[1]))
        #find the total changes and then the average
        dif = profits[85]-profits[0]
        avg = dif/85

            #greatest increase in profits
            #greatest decrease in profits
        for x in range(1,85):
            difference = profits[x]-profits[x-1]
            incdec.append(difference)
        
    #Print final answers
    print(f'Total months in dataset: {len(months)}')
    print(f'Total profits/losses over the period: ${total}')
    print(f'Change in profits/losses: ${dif}')
    print(f'Average change: ${avg:.2f}')
    print(f'Greatest increase: {months[incdec.index(int(max(incdec)))+1]} (${max(incdec)})')
    print(f'Greatest decrease: {months[incdec.index(int(min(incdec)))+1]} (${min(incdec)})')
                
    #Compile final answers in txt file
    outfile.write(f'Total months in dataset: {len(months)}\n')
    outfile.write(f'Total profits/losses over the period: ${total}\n')
    outfile.write(f'Change in profits/losses: ${dif}\n')
    outfile.write(f'Average change: ${avg:.2f}\n')
    outfile.write(f'Greatest increase: {months[incdec.index(int(max(incdec)))+1]} (${max(incdec)})\n')
    outfile.write(f'Greatest decrease: {months[incdec.index(int(min(incdec)))+1]} (${min(incdec)})')
