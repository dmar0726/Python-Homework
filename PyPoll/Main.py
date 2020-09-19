import os
import csv

Total = 0
Khan = 0
Correy = 0
Li = 0
OTooley = 0

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)

    for row in csvreader:

        Total = Total + 1

        if (row[2] == "Khan"):
            Khan = Khan + 1
        elif (row[2] == "Correy"):
            Correy = Correy + 1
        elif (row[2] == "Li"):
            Li = Li + 1
        else:
            OTooley = OTooley + 1

    Kahn_Percent = Khan / Total
    Correy_Percent = Correy / Total
    Li_Percent = Li / Total
    OTooley_Percent = OTooley / Total

    Winner = max(Khan, Correy, Li, OTooley)

    if Winner == Khan:
        Winner_name = "Khan"
    elif Winner == Correy:
        Winner_name = "Correy"
    elif Winner == Li:
        Winner_name = "Li"
    else:
        Winner_name = "O'Tooley"

print(f"Total Votes: {Total}")
print(f"Correy: {Correy_Percent}({Correy})")
print(f"Li: {Li_Percent}({Li})")
print(f"O'Tooley: {OTooley_Percent}({OTooley})")
print(f"Winner: {Winner_name}")