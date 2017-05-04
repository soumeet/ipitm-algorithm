'''Sayan_ipitm_test_6 v1.0
Partions a list of transactions according to their sizes.
Generates an IFM with the items and TID(transaction ids) and the rate of occurence.
Checks for identical transactions and if found, then the earliest TID is incremented
and the later one is deleted from the IFM'''
import csv
import bisect
from operator import add
transaction=[] #list of all the transactions
part=[] #'holds all the partitions according to size
item=[] #'All the items that are available'
mat=[] #'The IFM that is generated'
'Takes transacions from the csv and converts them into lists'
def read_t2():
	transaction.append([3,frozenset([2,3,5]),1])
	transaction.append([3,frozenset([2,3,1]),2])
	transaction.append([3,frozenset([2,3,1]),3])
	transaction.append([4,frozenset([1,2,3,5]),4])
	transaction.append([2,frozenset([2,3]),5])
	transaction.append([2,frozenset([2,1]),6])
	transaction.append([3,frozenset([1,2,3]),7])
	transaction.append([4,frozenset([4,2,3,5]),8])
	transaction.append([4,frozenset([1,2,3,4]),9])
	transaction.append([3,frozenset([2,3,5]),10])
	transaction.append([3,frozenset([6,7,8]),11])
	item.append(1)
	item.append(2)
	item.append(3)
	item.append(4)
	item.append(5)
	item.append(6)
	item.append(7)
	item.append(8)

def transactions():
    count=[]
    tid=1
    with open('dataset.csv', 'rb') as csvfile:
    	 spamreader = csv.reader(csvfile)
    	 for row in spamreader:
    		for i in row:
    			i=int(i)
    			if i not in item:
    				item.append(i)
    			count.append(i)
    		transaction.append([len(count),frozenset(count),tid])
    		count =[];tid=tid+1
    transaction.sort()
    print 1
'Partitions the transactions according to size'
def partition():
	size=[]
	transaction.sort()
	i=0
	while i<len(transaction):
		l=transaction[i][0]
		size.append(l)
		for j in range(i,len(transaction)):
			if transaction[j][0]>transaction[i][0]:
				i=j-1
				break
			else:
				size.append([transaction[j][2],transaction[j][1]])
				if j == len(transaction)-1 :
					i=j
		part.append(size)
		size=[]
		i=i+1
'Generates the IFM'
def gen_matrix():

	extra=[]
	item.sort()
	item.insert(0,'TID')
	#print item
	mat.append([item])
	extra=[0]*len(item)
	for j in range(len(transaction)):
		extra[0]=+transaction[j][2]
		for k in transaction[j][1]:
			m=bin_sort(k)
			extra[m]+=1
		mat.append(extra)
		extra=[]
		extra=[0]*len(item)
	mat[1:] = sorted(mat[1:])
'Deletes the identical entries and increases the first TID'
def ipitm():
    c=0
    for i in range(0,len(part)):
		for j in range(1,len(part[i])-1):
			for x in range(j+1,len(part[i])):
				if part[i][j][1]==part[i][x][1]:
					y = part[i][j][0]
					print y,part[i][x][0]
					mat[y][1:]=[z+1 if z!=0 else 0 for z in mat[y][1:]]
					mat[part[i][x][0]][1:]=[z-1 if z!=0 else 0 for z in mat[part[i][x][0]][1:]]

def ipistm():
	a=part
	for i in range(0,len(part)-1):
		for j in range(1,len(part[i])):
			for x in range(1,len(part[i+1])):
				if part[i][j][1].issubset(part[i+1][x][1]):
					print part[i+1][x][1],part[i][j][1]
					print mat[part[i+1][x][0]],mat[part[i][j][0]]
					mat[part[i+1][x][0]][1:]=map(add,mat[part[i+1][x][0]][1:],mat[part[i][j][0]][1:])
					mat[part[i][j][0]][1:]=[z-z if z!=0 else 0 for z in mat[part[i][j][0]][1:]]
					print mat[part[i+1][x][0]],mat[part[i][j][0]]
					break



'A binary search function usng the bisect module to find the index number of the item in the item list'
def bin_sort(n):
    i = bisect.bisect_left(item,n,1,len(item))
    if i!=len(item) and item[i]==n:
        return i
    else:
        return -2

transactions()
#read_t2()
partition()
gen_matrix()
ipitm()
ipistm()
