t = int(input())
expexted = [i for i in range(10**5)]
for p in range(t):
    n = int(input())
    ar = list(map(int,input().split()))
    flag = True
    trav = 0
    finalk = 1
    for i in range(1,n+1):
        k=i
        trav = 0 
        for j in range(n):
            if ar[j]==-1:
                continue
            elif ar[j]==(expexted[j]%k)+1:
                trav = 1
                continue
            else:
                trav = 0
                #print("break",i,j,trav,ar[j],(expexted[j]%k)+1)
                break

        if trav == 1:
            finalk = k
            break
    
    #print(finalk)
    
    for i in range(n):
        if ar[i]!=-1 and ar[i]!=(expexted[i]%finalk)+1:
            #print(ar[i],(expexted[i]%k)+1)
            flag = False
            break

    if flag and finalk==n:
        print("inf")
    elif flag:
        print(finalk)
    else:
        print("impossible")
