import sys
import csv
import numpy as np

dataset=sys.argv[1]
transactions=[] #transactions=[[tid, items[], sot]]
no_of_transactions=0
item_list=[]
no_of_items=0
max_sot=0
partitions=[] #partition=[[ pid, [tid, items[]], sot]]
ifm=[]

def read_transactions():
	with open(dataset, newline='') as csvfile:
            spamreader = csv.reader(csvfile)
            tid=1
            global max_sot
            for row in spamreader:
                transaction_row=[]
                for i in row:
                    item=int(i)
                    if item not in item_list:
                            item_list.append(item)
                    transaction_row.append(item)
                    transaction_size=len(transaction_row)
                    if max_sot<transaction_size:
                            max_sot=transaction_size
                transactions.append([tid,transaction_row,transaction_size])
                tid +=1

def partition_transactions():
		pid=1
		row=0
		c=0
		for sot in range(1,max_sot+1):
			transaction_list=[]
			while (row!=no_of_transactions and sot==transactions[row][2]):
				transaction_list.append([transactions[row][0],transactions[row][1]])
				row+=1
				c+=1
			partitions.append([pid, transaction_list, sot])
			pid+=1
		print(c)

def generate_ifm():
        for i in range(0, max_sot): 'loop through partition_id'
                sot=partitions[i][2]
                tid_count=len(partitions[i][1])
                ifm_row=[0]*1000
                for j in range(0, tid_count): 'loop through transaction_list'
                        #print(partitions[i][1][j][1], end='')
                        print(ifm_row)
                        for k in range(0, sot): 'loop through transaction_id'
                                #print(partitions[i][1][j][1][k]," ", end='')
                                print("tid: ", partitions[i][1][j][0], "item: ", partitions[i][1][j][1][k])

read_transactions()
no_of_transactions=len(transactions)
no_of_items=len(item_list)
#print(no_of_transactions)
#print(max_sot)
#print(no_of_items)
transactions.sort(key=lambda x: x[2])
for row in transactions:
        print(row)
'''for item in item_list:
        print(item)'''
partition_transactions()
'''for pid in partitions:
        print("pid: ",pid[0], " sot: ",pid[2])
        for tid in pid[1]:
                print(tid)'''
generate_ifm()
