import os
import csv

file = os.path.join('Resources','budget_data.csv')

with open(file, newline = '') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    header = next(csvreader)

    date_lst = []
    amount_lst = []
    profit_dic = {}

    for row in csvreader:
        date_lst.append(row[0])
        amount_lst.append(int(row[1]))
    
    for i in range(1,len(amount_lst)):
        if date_lst[i] not in profit_dic.keys():
            profit_dic[date_lst[i]] = amount_lst[i] - amount_lst[i-1]
        
    max_date = max(profit_dic, key = profit_dic.get)
    #Find the min value in the dictionary
    min_date = min(profit_dic, key = profit_dic.get)
    num_date = len(date_lst)
    total = sum(amount_lst)
    avg_change = round(sum(profit_dic.values())/(num_date - 1),2)

    txt_file = open("Summary Table.txt","w")

    txt_file.writelines(f"Financial Analysis\n---------------------\n")
    txt_file.writelines(f"Total Months: {num_date}\nTotal: ${total}\nAverage Change: ${avg_change}\n")
    txt_file.writelines(f"Greatest Increase in Profits: {max_date} (${profit_dic[max_date]})\n")
    txt_file.writelines(f"Greatest Decrease in Profits: {min_date} (${profit_dic[min_date]})")
    txt_file.close()

    print(f"Financial Analysis\n---------------------")
    print(f"Total Months: {num_date}\nTotal: ${total}\nAverage Change: ${avg_change}")
    print(f"Greatest Increase in Profits: {max_date} (${profit_dic[max_date]})")
    print(f"Greatest Decrease in Profits: {min_date} (${profit_dic[min_date]})")
