for i in range(int(input())):
    c,d,l = map(int,input().split())
    k = l/4
    if(d+c>=k):
        print("yes")
        break
    elif(k-d<=0):
        print("yes")
        break
    elif(c-(k-d)<=0):
        print("yes")
        break
    else:
        print("no")
        break

        