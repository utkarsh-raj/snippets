import math
n=input()
for i in range(n):
    k=input()
    c1=int(math.ceil(math.log(k,2)))
    c2=int(math.floor(math.log(k,2)))
 
    p1=pow(2,c1)
    p2=pow(2,c2)
 
    left=abs(k-p2)
    #print left
    if left==0:
        print 1
    else:
        d1=pow(2,int(math.ceil(math.log(left,2))))
        d2=pow(2,int(math.floor(math.log(left,2))))
        
 
        if d1==p2:
            d1=100000000001
        
        
        min1=abs(k-p2-1)
        min2=abs((p1+1)-k)
        min3=abs(left-d1)
        min4=abs(left-d2)
 
        #print min1 , min2, min3 , min4
        print min(min1,min2,min3,min4)
