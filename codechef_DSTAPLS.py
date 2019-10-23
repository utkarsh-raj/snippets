times = int(input())
for time in range(times):
    list1 = input()
    temp = list(map(int, list1.split()))
    N = temp[0]
    K = temp[1]
    z = N%(K*K)
    if z == 0:
        print("NO")
    else:
        print("YES")