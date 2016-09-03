'''Sayan_ipitm_test_6 v1.0
Partions a list of transactions according to their sizes.
Generates an IFM with the items and TID(transaction ids) and the rate of occurence.
Checks for identical transactions and if found, then the earliest TID is incremented
and the later one is deleted from the IFM'''
import csv
import bisect

transaction=[]'list of all the transactions'
part=[]'holds all the partitions according to size'
item=[]'All the items that are available'
mat=[]'The IFM that is generated'
'Takes transacions from the csv and converts them into lists'
def transactions():
    count=[]
    tid=1
    with open('T10I4D100K.csv', 'rb') as csvfile:
    	 spamreader = csv.reader(csvfile)
    	 for row in spamreader:
    		for i in row:
    			i=int(i)
    			if i not in item:
    				item.append(i)
    			count.append(i)
    		transaction.append([len(count),count,tid])
    		count =[];tid=tid+1
    transaction.sort()
'Partitions the transactions according to size'
def partition():
    size=[]
    transaction.sort()
    i=0
    while i < len(transaction):
        l=transaction[i][0]
        size.append(l)
        for j in range(i,len(transaction)):
            if transaction[j][0]>transaction[i][0]:
                i=j-1
                break
            else:
                size.append([transaction[j][2],transaction[j][1]])
        part.append(size)
        size = []
        i=i+1
'Generates the IFM'
def gen_matrix():
    extra=[]
    item.sort()
    item.insert(0,'TID')'Item list is modified for better access to IFM list'
    mat.append(item)
    extra=[0]*len(item)
    for j in range(len(transaction)):
        for k in transaction[j][1]:
            m=bin_sort(k)
            extra[m]=extra[m]+1
        mat.append([j+1,extra])
        extra=[0]*len(item)
'Deletes the identical entries and increases the first TID'
def ipitm():
    for i in range(0,len(part)):
        for j in range(1,len(part[i])-1):
            for x in range(j+1,len(part[i][j])):
                if part[i][j][1]==part[i][x][1]:
                    y=part[i][j][0]
                    print y
                    mat[y]=[z*2 for z in mat[y]]
                    del mat[part[i][x][0]]

'A binary search function usng the bisect module to find the index number of the item in the item list'
def bin_sort(n):
    i = bisect.bisect_left(item,n,1,len(item))
    if i!=len(item) and item[i]==n:
        return i
    else:
        return -2

transactions()
partition()
gen_matrix()
ipitm()