#Chef and Card Trick
t = int(input())
for p in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    drop = 0
    firstlow = arr[0]
    secondhigh = arr[n-1]
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            drop+=1
    if drop == 0:
        print("YES")
    elif drop == 1:
        if firstlow>=secondhigh:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
