t=int(input())
for i in range(t):
	n,a,b=map(int,input().split())
	phi=list(map(int,input().split()))
	print((phi.count(a)*phi.count(b))/n**2)
  
  #Contributed by Ankush Jain
