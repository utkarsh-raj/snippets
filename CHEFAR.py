t=int(input())
for i in range(0,t):
    n,k=list(map(int,input().strip().split()))
    a=list(map(int,input().strip().split()))
    less_k=n-(a.count(1))
    if(less_k<=k):
        print("YES")
    else:
        print("NO")
