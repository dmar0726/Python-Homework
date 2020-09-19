import os
import csv

csvpath = os.path.join("..", "PyBank","Resources", "budget_data.csv")

total_months = 0
total_profit_loss = 0
prev_profit_loss = 0
month_change = 0
total_month_change = 0
average_month_change = 0
greatest_increase = 0
greatest_increase_month = ""
greatest_decrease = 0
greatest_increase_month = ""

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvreader)
    
    for row in csvreader:
        total_months = total_months + 1
        
        total_profit_loss = total_profit_loss + int(row[1])

        if total_months > 1:
            month_change = int(row[1]) - prev_profit_loss
        
        total_month_change = total_month_change + month_change
        
        prev_profit_loss = int(row[1])
        
        if month_change > greatest_increase:
            greatest_increase = month_change
            greatest_increase_month = row[0]
        
        if month_change < greatest_decrease:
            greatest_decrease = month_change
            greatest_decrease_month = row[0]


average_month_change = total_month_change / (total_months - 1)
        
print("Financial Analysis")
print("---------------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(total_profit_loss))
print("Average Change: $" + str(round(average_month_change,2)))
print("Greatest Increase " + greatest_increase_month + " $" + str(greatest_increase))
print("Greatest Decrease " + greatest_decrease_month + " $" + str(greatest_decrease))

Text_output = (
"Financial Analysis\n"
"---------------------------\n"
f"Total Months: {total_months}\n"
f"Total: ${total_profit_loss}\n"
f"Average Change: ${round(average_month_change,2)}\n"
f"Greatest Increase  + greatest_increase_month + {greatest_increase}\n"
f"Greatest Decrease  + greatest_decrease_month + {greatest_decrease}\n"
)

file="PyBank_analysis.txt"
with open(file, "w") as text:
    text.write(Text_output)
    text.close