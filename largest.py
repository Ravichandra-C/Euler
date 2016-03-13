def mul(x,y):
    return x*y
num= 10
list_1=[2]
i=3

while i<num:
    prime=True

    for j in list_1:
        if j<i/2:
            if i%j==0:
                prime=False
                break
    if prime==True:
        list_1.append(i)
    i+=1
print list_1

print reduce(mul,list_1)

