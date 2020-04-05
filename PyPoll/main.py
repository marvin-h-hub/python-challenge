import os
import csv

file = os.path.join('Resources','election_data.csv')

with open(file, newline = '') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    header = next(csvreader)


    voter_lst = []
    short_lst = []
    candidate_lst = []
    c_dic = {}

    for row in csvreader:
     
        voter_lst.append(row[0])
        candidate_lst.append(row[2])
        if row[2] not in short_lst:
            short_lst.append(row[2])
    
    total_vote = len(voter_lst)

    for i in short_lst:
        c_dic[i] = int(candidate_lst.count(i))
    
    winner = max(c_dic, key = c_dic.get)

 
    txt_file = open("Summary Table.txt","w")
   
    txt_file.writelines(f"Election Results\n-------------------------\n")
    txt_file.writelines(f"Total Votes:{total_vote}\n-------------------------\n")
    for i in short_lst:
        txt_file.writelines(f"{i}: {round(c_dic[i]/total_vote*100,2)}% ({c_dic[i]})\n")
    txt_file.writelines(f"-------------------------\nWinner: {winner}\n-------------------------")
    txt_file.close()


print(f"Election Results\n-------------------------")
print(f"Total Votes:{total_vote}\n-------------------------")
for i in short_lst:
    print(f"{i}: {round(c_dic[i]/total_vote*100,2)}% ({c_dic[i]})")
print(f"-------------------------\nWinner: {winner}\n-------------------------")