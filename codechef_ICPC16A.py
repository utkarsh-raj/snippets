t=int(input())
for i in range(t):
	x1,y1,x2,y2=map(int,input().split())
	if x1==x2 and y2>y1:
		print("up")
	elif x1==x2 and y2<y1:
		print("down")
	elif y1==y2 and x2>x1:
		print("right")
	elif y1==y2 and x2<x1:
		print("left")
	else:
		print("sad")
		
    #Contributed by Ankush Jain
