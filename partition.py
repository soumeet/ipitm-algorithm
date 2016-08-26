import sys
import csv

dataset=sys.argv[1]
transactions=[[0,[]]]
no_of_transactions=0
partition=[]
def read_transactions():
	with open(dataset, newline='') as csvfile:
            spamreader = csv.reader(csvfile)
            tid=1
            for row in spamreader:
                transaction_row=[]
                for i in row:
                    item=int(i)
                    transaction_row.append(item)
                transactions.append([tid,transaction_row])
                tid +=1

read_transactions()
no_of_transaction=len(transactions)
#print(no_of_transaction)
#print(transactions)