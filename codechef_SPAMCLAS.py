t=int(input())
for i in range(t):
	n,minx,maxx=map(int,input().split())
	one=1
	all=minx%2
	for j in range(n):
		a,b=map(int,input().split())
		one=one*(a%2)
		all=(a*all+b)%2
	span=(maxx-minx+1)%2
	ran=maxx-minx+1
	if span==0 and one==1:
		print(int(ran/2)," ",int(ran/2))
	elif one==0 and all==0:
		print(int(ran)," ",0)
	elif one==0 and all==1:
		print(0," ",int(ran))
	elif span==1 and one==1 and all==0:
		print(int(ran/2)+1," ",int(ran/2))
	else:
		print(int(ran/2)," ",int(ran/2)+1)
    
    
    #Contributed by Ankush Jain
