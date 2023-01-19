# Dependencies
import os
import csv
import numpy

# Lists to store data
months=[]
profitloss=[]

# Set the path for the file
PyBank_csvpath = os.path.join("Resources","budget_data.csv")

# Open the CSV
with open(PyBank_csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    csv_header = next(csvreader)
       
# Loop through data to update list
    for row in csvreader:
        # Add months to months list
        months.append(row[0])
        # Add each month's profitloss to the profitloss list 
        profitloss.append(int(row[1]))
    
    # Calulating Total Months
    total_months =len(months)
    # Calculating net total amount of profit/loss over the entire peiod
    profitloss_total = sum(profitloss)
    # Creating a list to store and calulate monthly change of profit/loss 
    months_change = numpy.diff(profitloss)
    # Calculating average of monthly change of profit/loss
    average_change = round(sum(months_change)/len(months_change),2)
    # Calculating greatest increase in profits in amount over the entire period
    greatest_increase_in_profits = max(months_change)
    # Calculating greatest decrease in profits in amount over the entire period
    greatest_decrease_in_profits = min(months_change)
    # Calculating greatest increase in profits date
    change_month_increase= months[int(numpy.where(months_change==greatest_increase_in_profits)[0])+1]
     # Calculating greatest decrease in profits date
    change_month_decrease= months[int(numpy.where(months_change==greatest_decrease_in_profits)[0])+1]
  
   
# Specify the file to write to   
output_file =os.path.join("analysis","PyBank_results.txt")

# Open the file using write mode to create a text file and print analysis in it
with open(output_file, "w") as f:
    f.write("Financial Analysis \n\n")
    f.write("------------------------------------------------------ \n\n")
    f.write("Total Months: " + str(total_months)+ "\n\n")
    f.write("Total: $" + str(profitloss_total)+ "\n\n")
    f.write("Average Change: $"+ str(average_change)+ "\n\n")
    f.write("Greatest Increase in Profits: "+change_month_increase+ " ($"+ str(greatest_increase_in_profits)+")"+"\n\n")
    f.write("Greatest Decrease in Profits: "+change_month_decrease+ " ($"+ str(greatest_decrease_in_profits)+")"+"\n\n")
    
# Printing analysis to the terminal  
    print("Financial Analysis" )
    print("------------------------------------------------------")
    print("Total Months: " + str(total_months))
    print("Total: $" + str(profitloss_total))
    print("Average Change: $"+ str(average_change))
    print("Greatest Increase in Profits: "+change_month_increase+ " ($"+ str(greatest_increase_in_profits)+")")
    print("Greatest Decrease in Profits: "+change_month_decrease+ " ($"+ str(greatest_decrease_in_profits)+")")

