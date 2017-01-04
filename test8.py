import sys
import csv
import time
import numpy as np

dataset=sys.argv[1]
no_of_transactions=0

t=np.zeros((1000,1000))
start_time=time.time()
'''
with open(dataset, newline='') as csvfile:
        i=0
        j=0
        spamreader = csv.reader(csvfile)
        for row in spamreader:
                j=0
                for item in row[1:]:
                        t[i][j]=row[j]
                        j+=1
                i+=1
#print(t)
np.savetxt("out8.csv", t, '%5f', delimiter=",")
'''

out8=csv.writer(open("out8.csv","w"), delimiter=',',quoting=csv.QUOTE_ALL)
with open(dataset, newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
                out8.writerow(row[1:])

print("execution time: ", time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time)))

