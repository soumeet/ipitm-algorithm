import sys
import csv
import time
import numpy as np

dataset=sys.argv[1]
transactions=[] #transactions=[tid, items[]]
no_of_transactions=0

def read_transactions():
	with open(dataset, newline='') as csvfile:
            spamreader = csv.reader(csvfile)
            for row in spamreader:
                transactions.append([int(row[0]),row[1:]])

def sim(l1, l2):
        return ((len(set(l1).intersection(l2)))/(len(set(l1).union(l2))))

start_time=time.time()
read_transactions()
no_of_transactions=len(transactions)
print(no_of_transactions)
#print(transactions)

for i in range(no_of_transactions):
        for j in range(i+1,no_of_transactions):
                print(transactions[i], " and ", transactions[j], "sim: ", sim(transactions[i][1],transactions[j][1]))

print("execution time: ", time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time)))

