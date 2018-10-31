for t in range(input()):
    n,m = map(int, raw_input().split())
    l=[]
    for i in range(n):
        l.append(list(raw_input()))
    l2 = []
    flag = 0
    for i in range(n):
        if i==0 or i==n-1:
            l3 = [1]+[2]*(m-2) + [1]
        else:
            l3 = [2]+[4]*(m-2) + [2]
        l2.append(l3)
        
    for i in range(n-1):
        for j in range(m-1):
            if l[i][j] =="#" or l[i+1][j] == "#" or l[i][j+1] == "#" or l[i+1][j+1] =="#":
                l2[i][j] -=1 
                l2[i+1][j] -=1 
                l2[i][j+1] -=1
                l2[i+1][j+1] -=1
    
    for i in range(n):
        for j in range(m):
            if l2[i][j] == 0 and l[i][j] == ".":
                flag = 1 
                break
        if flag == 1:
            break
    if flag == 1:
        print "NO"
    else:
