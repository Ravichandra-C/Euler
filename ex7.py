from math import sqrt,floor
import time


start=time.clock()
list_1=[2]
num=10001
i=3
while len(list_1)<num:
    prime=True
    count_i=int(sqrt(i)+1)
    #print (count_i)
    #for j in list_1:
    for j in range(2,count_i):
        if  i%j==0:
            prime=False
            break
    
    if prime==True:
        list_1.append(i)
    i+=2
print list_1.pop()
print "Time taken to complete:",time.clock()-start
