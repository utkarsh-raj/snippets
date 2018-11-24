t=int(raw_input())
arr=[['b','o','b'],['b','b','o'],['o','b','b']]
while (t>0 and t<=20000):
    str1=raw_input()
    str2=raw_input()
    c=0
    for i in range(0,3):
        c=0
        for j in range(0,3):
        	if str2[j]==arr[i][j] or str1[j]==arr[i][j]:
        	    c+=1
        if c==3:
            break
    t-=1
    if c==3:
        print "yes"
    else:
        print "no"
