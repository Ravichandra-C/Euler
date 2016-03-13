from math import sqrt,ceil
from sys import exit
import time
start_time=time.clock()
num=600851475143
#num=10201648
num_comp=num/2
i=2
quo=num
list_1=[]
while i<=num_comp:
    #print i
    if(num%2!=0 and i%2==0):
        i+=1 
        #print " increment as not even number"   
    if num%i==0 and num!=0:
        num=num/i
        print i,"*",num,"=",num*i
        print num,"is new quotient"
        print i,"is a factor"
        num_comp=num/2
        #print num    
        list_1.append(i)
        i=1
            
    i+=1 
list_1.append(num)    
print list_1
list_1.reverse()
print list_1

print "time taken to execute",time.clock()-start_time


for prime_num in list_1:
    sq_num=sqrt(prime_num)
    for i in range(2,ceil(sqrt(prime_num))):
           if (prime_num % i) == 0:
               print(prime_num,"is not a prime number")
               print(i,"times",prime_num//i,"is",prime_num)
               break
           else:
               print("%d is a Largest Prime" ) %(prime_num)
               exit(0)

