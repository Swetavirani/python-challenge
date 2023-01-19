# Dependencies
import os
import csv

# Lists to store data
Ballot_IDs=[]
Candidates=[]
Unique_Canditate_Names =[]
Vote_Counter_by_Candidate=[]

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
    
    #Creating Unique list of Candidate Names and sorting them alphabetically
    Unique_Canditate_Names =sorted(set(Candidates))
         
    # Defining function to print analysis by candidate and winner name to the terminal
    def list_of_candidates():
        
        for Candidate in Unique_Canditate_Names:
            Vote_Counter =0
            Vote_Counter += Candidates.count(Candidate)
            Vote_Percentage = round((Vote_Counter/total_votes)*100,3)
            Vote_Counter_by_Candidate.append(Vote_Counter)
            highest_votes = Vote_Counter_by_Candidate.index(max(Vote_Counter_by_Candidate))
            Winner= Unique_Canditate_Names[int(highest_votes)]
            print(f'{Candidate}: {Vote_Percentage}%  ({Vote_Counter})')
        print("------------------------------------------------------")
        print(f'Winner: {Winner}')
        print("------------------------------------------------------")


    # Defining function to print analysis by candidate and winner name to the text file       
    def list_of_candidates_txtfile():
        
        for Candidate in Unique_Canditate_Names:
            Vote_Counter =0
            Vote_Counter += Candidates.count(Candidate)
            Vote_Percentage = round((Vote_Counter/total_votes)*100,3)
            Vote_Counter_by_Candidate.append(Vote_Counter)
            highest_votes = Vote_Counter_by_Candidate.index(max(Vote_Counter_by_Candidate))
            Winner= Unique_Canditate_Names[int(highest_votes)]
            f.write(f'{Candidate}: {Vote_Percentage}%  ({Vote_Counter})\n\n')
        f.write("------------------------------------------------------ \n\n")
        f.write(f'Winner: {Winner}\n\n')
        f.write("------------------------------------------------------ \n\n")
     
               
#Specify the file to write to   
output_file = os.path.join("analysis","PyPoll_results.txt")

#Open the file using write mode to create a text file and print analysis in it
with open(output_file, "w") as f:
    f.write("Election Results \n\n")
    f.write("------------------------------------------------------ \n\n")
    f.write("Total Votes: " + str(total_votes)+ "\n\n")
    f.write("------------------------------------------------------ \n\n")
    list_of_candidates_txtfile()
 
#Printing analysis to the terminal  
    print("Election Results" )
    print("------------------------------------------------------")
    print("Total Votes: " + str(total_votes))
    print("------------------------------------------------------")
    list_of_candidates()
    