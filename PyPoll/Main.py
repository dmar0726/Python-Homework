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

    Khan_Percent = Khan / Total
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

print("Election Results")
print("---------------------------")
print(f"Total Votes: {Total}")
print("---------------------------")
print(f"Khan: {round(Khan_Percent*100,3)}%({Khan})")
print(f"Correy: {round(Correy_Percent*100,3)}%({Correy})")
print(f"Li: {round(Li_Percent*100,3)}%({Li})")
print(f"O'Tooley: {round(OTooley_Percent*100,3)}%({OTooley})")
print("---------------------------")
print(f"Winner: {Winner_name}")

Text_output = (
"Election Results\n"
"---------------------------\n"
f"Total Votes: {Total}\n"
"---------------------------\n"
f"Khan: {round(Khan_Percent*100,3)}%({Khan})\n"
f"Correy: {round(Correy_Percent*100,3)}%({Correy})\n"
f"Li: {round(Li_Percent*100,3)}%({Li})\n"
f"O'Tooley: {round(OTooley_Percent*100,3)}%({OTooley})\n"
"---------------------------\n"
f"Winner: {Winner_name}\n"
)

file="PyPoll_analysis.txt"
with open(file, "w") as text:
    text.write(Text_output)
    text.close