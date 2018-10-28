#Chefland and Average Distance
t = int(input())
for p in range(t):
    n,m = list(map(int,input().split()))
    matrix = []
    for i in range(n):
        arr = list(map(int,list(input())))
        matrix.append(arr)
    hash1 = [0 for i in range(n+m-2)]
    hash2 = [0 for i in range(n+m-2)]
    hash3 = [0 for i in range(n+m-2)]
    hash4 = [0 for i in range(n+m-2)]
    
    hashar = [0 for i in range(n+m-2)]
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==1:
                if i+j>=0:
                    hash1[i+j]+=1
                else
    
    for i in range(len(cord)):
        for j in range(i+1,len(cord)):
            #print(cord[i],cord[j])
            hashar[abs(cord[i][1]-cord[j][1]) + abs(cord[i][0]-cord[j][0])-1] += 1
    print(*hashar)
