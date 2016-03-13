import time
start=time.clock()
sum=0
target_num=101
for a in range(1,target_num):
    for b in range(a+1,target_num):
        sum+=a*b
        #print sum

print "Result:",sum*2
print "Total Time taken:",time.clock()-start
