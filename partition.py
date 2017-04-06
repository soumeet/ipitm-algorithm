import sys
import csv
import time
import traceback
import numpy as np

start_time=time.time()
dataset=sys.argv[1]
transactions=[] #transactions=[[tid, items[], sot]]
no_of_transactions=0
items_list=[]
no_of_items=0
max_sot=0
partitions=[] #partition=[[ pid, [TID, items[]], sot, identicalTID]]
ifm=np.array([])

'''
def csv_writer():
	out_partition=csv.writer(open("out_parition.csv","w"), delimiter=',',quoting=csv.QUOTE_ALL)
	out_partition.writerow(['PartitionID','TID','Items','SOT'])
	for row in spamreader:
		out_partition.writerow(row[1:])
'''

def sim(l1, l2):
	return ((len(set(l1).intersection(l2)))/(len(set(l1).union(l2))))


def read_transactions():
	with open(dataset, newline='') as csvfile:
            spamreader = csv.reader(csvfile)
            tid=1
            global max_sot
            for row in spamreader:
                transaction_row=[]
                for i in row[1:]:
                    item=int(i)
                    if item not in items_list:
                            items_list.append(item)
                    transaction_row.append(item)
                    transaction_size=len(transaction_row)
                    if max_sot<transaction_size:
                            max_sot=transaction_size
                transactions.append([tid,transaction_row,transaction_size])
                tid +=1

def partition_transactions():
		transactions.sort(key=lambda x: x[2])
		pid=1
		row=0
		for sot in range(1,max_sot+1):
			transaction_list=[]
			while (row!=no_of_transactions and sot==transactions[row][2]):
				transaction_list.append([transactions[row][0],transactions[row][1]])
				row+=1
			partitions.append(["p"+str(pid), transaction_list, sot])
			pid+=1

def generate_ifm():
		global ifm
		transactions.sort(key=lambda x: x[0])
		#ifm=[[0]*(no_of_items+1)]*no_of_transactions
		ifm=np.zeros((no_of_transactions+1,no_of_items+1))
		for i in range(no_of_items):
			ifm[0,i+1]=i
		for i in range(no_of_transactions+1):
			ifm[i,0]=i

		for i in range(1,no_of_transactions):
			tid=transactions[i][0]
			transaction_list=transactions[i][1]
			for items in transaction_list:
				ifm[tid][items+1]+=1

def ipitm():
	global ifm
	for i in range(2,max_sot):
		sot=partitions[i][2]
		tid_count=len(partitions[i][1])
		c=0
		for j in range(len(partitions[i][1])):
			identical=[]
			try:
				for k in range(j+1,len(partitions[i][1])):
					if sim(partitions[i][1][j][1],partitions[i][1][k][1])==1.0:
						for items in partitions[i][1][j][1]:
							ifm[partitions[i][1][j][0],items+1]+=1
							identical.append(partitions[i][1][k][0])
							ifm=np.delete(ifm,(list(ifm[:,0]).index(partitions[i][1][k][0])),0)
							del partitions[i][1][k]
			except:
				#traceback.print_exc()
				partitions[i][1][j].append(identical)
				continue


read_transactions()
no_of_transactions=len(transactions)
no_of_items=len(items_list)
print("no of transactions: ",no_of_transactions)
print("maximum size of transaction: ",max_sot)
print("total no items: ",no_of_items)
print("items list: ",items_list)


partition_transactions()
out_partition=csv.writer(open("partition.csv","w"), delimiter=',',quoting=csv.QUOTE_ALL)
out_partition.writerow(['PartitionID','TID','Items','SOT'])
for pid in partitions:
		#print(pid)
        #print("pid: ",pid[0], " sot: ",pid[2])
        f=0
        for tid in pid[1]:
            #print(tid)
            if f==0:
            	out_partition.writerow([pid[0],tid[0],tid[1],pid[2]])
            	f+=1
            else:
            	out_partition.writerow(['',tid[0],tid[1],''])

generate_ifm()
np.savetxt("ifm.csv",ifm,delimiter=",")

ipitm()
out_partition=csv.writer(open("partition_updated.csv","w"), delimiter=',',quoting=csv.QUOTE_ALL)
out_partition.writerow(['PartitionID','TID','Items','IdenticalTID'])
for pid in partitions:
        f=0
        for tid in pid[1]:
            if f==0:
            	out_partition.writerow([pid[0],tid[0],tid[1],pid[2]])
            	f+=1
            else:
            	if len(tid)==3:
            		out_partition.writerow(['',tid[0],tid[1],tid[2]])
            	else:
            		out_partition.writerow(['',tid[0],tid[1],''])

np.savetxt("ifm_updated.csv",ifm,delimiter=",")
print("execution time: ", time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time)))
