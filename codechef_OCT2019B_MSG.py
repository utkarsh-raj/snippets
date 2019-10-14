#for functions
#auther @Saurabh_Pandey
def value(B,Y):
    res=0
    for j in range(0,len(Y)):
            if(ord(Y[j])>=65):
                val=ord(Y[j])-55
                res+=val*(B**(len(Y)-j-1))
                
            else:
                val=int(Y[j])
                res+=val*(B**(len(Y)-j-1))
    return res
 
def minbase(Y):
    mbase=0
    for j in range(0,len(Y)):
        if(ord(Y[j])>=65):
            val=ord(Y[j])-55
            if(val>mbase):
                mbase=val
        else:
            val=int(Y[j])
            if(val>mbase):
                mbase=val
    return mbase+1
#end fucntion are

test=int(input())
for iii in range(0,test):
    N=int(input())
    B1=[]
    B2=[]
    Y1=[]
    Y2=[]
    for i in range(0,N):
        a2=input()
        a1=a2.split()
        if(int(a1[0])!=-1):
            B1.append(int(a1[0]))
            Y1.append(a1[1])
        else:
            B2.append(int(a1[0]))
            Y2.append(a1[1])
    
    result=-1
    flag1=0
    bflag='True'
    for j in range(0,len(B1)):
        val=value(B1[j],Y1[j])
        if(j==0):
            result=val
        if(j>0):
            if(result==val):
                continue
            else:
                result=-1
                bflag='False'
                break
                
    if(bflag=='True'):
        if(result!=-1):
            b1flag='True'
            for k in range(0,len(B2)):
                if(b1flag=='False'):
                    break
                mbase=minbase(Y2[k])
                for l in range(mbase,37):
                    val=value(l,Y2[k])
                    if(result==val):
                        break
                    elif(l==36):
                        result=-1
                        b1flag='False'
                        break
                
        else:
            mbase=minbase(Y2[0])
            kflag=0
            for m in range(mbase,38):
                if(kflag==1):
                #this will execute when all values satisfires for rest of Y2
                    break
                if(m==37):
                    result=-1
                    break
                result=value(m,Y2[0])
                if(len(Y2)==1):
                    break
                b1flag='True'
                for k in range(1,len(Y2)):
                    if(b1flag=='False'):
                        break
                    mbase=minbase(Y2[k])
                    for l in range(mbase,37):
                        val=value(l,Y2[k])
                        if(result==val):
                            if(k==(len(Y2)-1)):
                                kflag=1
                            break
                        elif(l==36):
                            #result=-1
                            b1flag='False'
                            break
    if(result>(10**12)):
        print('-1')
    else:  
        print(result)
    