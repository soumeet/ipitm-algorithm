import sys
import csv
import time
import numpy as np
import pandas as pd


dataset=sys.argv[1]
#transactions=[] #transactions=[tid, items[]]
no_of_transactions=0

'''
def read_transactions():
	with open(dataset, newline='') as csvfile:
            spamreader = csv.reader(csvfile)         
            for row in spamreader:
                transactions.append([int(row[0]),row[1:]])
'''

def similarity(l1, l2):
        tmp=((len(set(l1).intersection(l2)))/(len(set(l1).union(l2))))
        return tmp

start_time=time.time()
#read_transactions()


df=pd.read_csv(dataset,index_col=0)

'''
sim=np.zeros((no_of_transactions,no_of_transactions))
for i in range(no_of_transactions):
        for j in range(i+1,no_of_transactions):
                #print(transactions[i], " and ", transactions[j], "sim: ", similarity(transactions[i][1],transactions[j][1]))
                sim[i][j]=similarity(transactions[i][1],transactions[j][1])
np.savetxt("out7.csv", sim, '%2.3f', delimiter=",")
'''
print("execution time: ", time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time)))
