ar = []
for i in range(1,10**5+1):
    ar.append(bin(i)[2:].count('1'))
t = int(input())
for p in range(t):
    a,b,c = list(map(int,input().split()))
    count = 0
    aBin = ar[a-1]
    bBin = ar[b-1]
    for i in range(1,c):
        j = c-i
        n1 = ar[i-1]
        n2 = ar[j-1]
        if n1==aBin and n2==bBin:
            count += 1
            #print(n1,n2,aBin,bBin)
    print(count)
