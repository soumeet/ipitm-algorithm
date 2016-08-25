import csv
transaction=[]
transaction_part=[]
item=[[0,[]]]
c2=1
def transactions():
	count=[]
	with open('T10I4D100K.csv', 'rb') as csvfile:
    	 spamreader = csv.reader(csvfile)
    	 for row in spamreader:
    		for i in row:
    			i=int(i)
    			if i not in item:
    				item.append(i)
    			count.append(i)
    		transaction.append(count)
    		count =[]

def partition():
 	size = []
 	c = 0
 	for i in range(len(transaction)):
         size.append(len(transaction[0]))
         for j in range(i+1,len(transaction)):
             if size[i]== len(transaction[j]):
                 transaction_part[c].append(size[i])
                 if transaction[i] not in transaction_part[c]:
                     transaction_part[c][c1].append(transaction[i])
                 transaction_part[c].append(list(transaction[j]))
                 c=c+1

transactions()
partition()
print len(transaction[0])




