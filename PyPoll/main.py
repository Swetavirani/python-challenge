# Dependencies
import os
import csv

# Lists to store data
Ballot_IDs=[]
Candidates=[]
Unique_Canditate_Names =[]
Votes_Candidate={}

# Set the path for the file
PyBank_csvpath = os.path.join("Resources","election_data.csv")

# Open the CSV
with open(PyBank_csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    csv_header = next(csvreader)
           
# Loop through data to update lists
    for row in csvreader:
        # Add votes casted 
        Ballot_IDs.append(row[0])
        # Add Candidates names to the list 
        Candidates.append(row[2])

     # Calulating Total Votes
    total_votes =len(Ballot_IDs)
    # Finding the unique candidates names
    Unique_Canditate_Names=set(Candidates)

           
#Specify the file to write to   
output_file =os.path.join("analysis","PyPoll_results.txt")

#Open the file using write mode to create a text file and print analysis in it
with open(output_file, "w") as f:
    f.write("Election Results \n\n")
    f.write("------------------------------------------------------ \n\n")
    f.write("Total Votes: " + str(total_votes)+ "\n\n")
    f.write("------------------------------------------------------ \n\n")
    print(*Unique_Canditate_Names, sep ="\n\n\n",file = f) 
    f.write("------------------------------------------------------ \n\n")
    f.write("Winner: " + "\n\n")
    f.write("------------------------------------------------------ \n\n")

#Printing analysis to the terminal  
    print("Election Results" )
    print("------------------------------------------------------")
    print("Total Votes: " + str(total_votes))
    print("------------------------------------------------------")
    print(*Unique_Canditate_Names, sep ="\n\n") 
    print("------------------------------------------------------")
    print("Winner: ")
    print("------------------------------------------------------")