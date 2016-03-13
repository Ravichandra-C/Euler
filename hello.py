def f(x): 
    return (x%2==0) 
def add(x,y): 
    return x+y
list=[1,2]
c=3
while c<4000000:
    c=add(list[-1],list[-2])
    list.append(c)
New_list=filter(f,list)
print reduce(add,New_list)
