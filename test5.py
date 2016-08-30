import csv
import bisect
transaction=[]
part=[]
item=[]

def transactions():
    count=[]
    j=1
    with open('T10I4D100K.csv', 'rb') as csvfile:
    	 spamreader = csv.reader(csvfile)
    	 for row in spamreader:
			for i in row:
				i=int(i)
    			if i not in item:
    				item.append(i)
    			count.append(i)
    		transaction.append([len(count),count,j])
    		count =[];j=j+1
    transaction.sort()

def partition():
    size=[]
    transaction.sort()
    i=0
    while i < len(transaction):
        l=transaction[i][0]
        size.append(l)
        for j in range(i,len(transaction)):
            if transaction[j][0]>transaction[i][0]:
                i=j
                break
            else:
                size.append([transaction[j][2],transaction[j][1]])
        part.append(size)
        size = []
        i=i+1

def gen_matrix():
    mat=[]
    extra=[]
    item.sort()
    item.insert(0,'TID')
    mat.append(item)
    extra=[0]*1000
    for j in range(len(transaction)):
        for k in transaction[j][1]:
            m=bin_sort(k)
            extra[m]=extra[m]+1
        mat.append([j+1,extra])
        extra=[0]*1000

def bin_sort(n):
    i = bisect.bisect_left(item,n,1,len(item))
    if i!=len(item) and item[i]==n:
        return i
    else:
        return -2

transactions()
partition()
gen_matrix()
