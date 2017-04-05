import sys
import csv
import time
import numpy as np

start_time=time.time()
dataset=sys.argv[1]
transactions=[] #transactions=[[tid, items[], sot]]
no_of_transactions=0
items_list=[]
no_of_items=0
max_sot=0
partitions=[] #partition=[[ pid, [tid, items[]], sot]]
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
		ifm=np.zeros((no_of_transactions,no_of_items))


		for i in range(no_of_transactions):
			tid=transactions[i][0]
			transaction_list=transactions[i][1]
			for items in transaction_list:
				ifm[tid-1][items]+=1

def ipitm():
'''
        for i in range(0, max_sot):
        	sot=partitions[i][2]
        	tid_count=len(partitions[i][1])
        	ifm_row=[0]*1000
        	for j in range(0, tid_count):
        		#print(partitions[i][1][j][1], end='')
        		print(ifm_row)
        		for k in range(0, sot):
        			#print(partitions[i][1][j][1][k]," ", end='')
        			print("tid: ", partitions[i][1][j][0], "item: ", partitions[i][1][j][1][k])
'''

read_transactions()
no_of_transactions=len(transactions)
no_of_items=len(items_list)
print("no of transactions: ",no_of_transactions)
print("maximum size of transaction: ",max_sot)
print("total no items: ",no_of_items)
print("items list: ",items_list)
'''
for row in transactions:
        print(row)
'''

partition_transactions()

out_partition=csv.writer(open("out_partition.csv","w"), delimiter=',',quoting=csv.QUOTE_ALL)
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
np.savetxt("out_ifm.csv",ifm,delimiter=",")
print("execution time: ", time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time)))