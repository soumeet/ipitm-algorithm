import sys
import csv

dataset=sys.argv[1]
transactions=[[0,[],0]] #transactions=[[tid, items[], sot]]
no_of_transactions=0
max_sot=0
partitions=[[0,[0,[]],0]] #partition=[[ pid, [tid, items[]], sot]]
def read_transactions():
	with open(dataset, newline='') as csvfile:
            spamreader = csv.reader(csvfile)
            tid=1
            for row in spamreader:
                transaction_row=[]
                for i in row:
                    item=int(i)
                    transaction_row.append(item)
                    transaction_size=len(transaction_row)
                transactions.append([tid,transaction_row,transaction_size])
                tid +=1

def partition_transactions():
		pid=1
		i=1
		for sot in range(1,25):
                        transaction_list=[]
                        while (i!=no_of_transactions and sot==transactions[i][2]):
                                transaction_list.append([transactions[i][0],transactions[i][1]])
                                i+=1
                        partitions.append([pid, transaction_list, sot])
                        pid+=1

read_transactions()
no_of_transactions=len(transactions)
#print(no_of_transactions)
transactions.sort(key=lambda x: x[2])
for row in transactions:
        print(row)
partition_transactions()
for pid in partitions:
        print("pid: ",pid[0], " sot: ",pid[2])
        for tid in pid[1]:
                print(tid)
