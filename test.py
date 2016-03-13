pali_list=[]
print 999*499
print 500*500
pali_old="10000"
for i in range(101,999):

    for j in range(101,999):
    
        result=i*j
        #print result ,"is result"
        res_str=str(result)
        res_str_1=res_str[::-1]
        #print res_str,"===",res_str_1
        if(res_str_1==res_str):
            pali_new=res_str
            if int(pali_new)>int(pali_old):
                pali_old=pali_new
                print "New highest palindrome %s" %(pali_old)
print pali_old
