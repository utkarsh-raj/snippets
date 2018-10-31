t = int(input())

def cal(n,k):
	if n < (k*(k+1)/2):
		return -1
	
	A = [0]*k
	A[k//2] = n//k
for i in range(k//2+1,k):
		A[i] = A[i-1]+1

	for i in range(k//2-1,-1,-1):
		A[i] = A[i+1] - 1
	l = sum(A)
	# print(A,l)
	
	if l < n:
		c = n-l
		i = k-1
		while c:
			A[i]+=1
			if i==-1:
				i=k-1
			i-=1
			c-=1 
	else:
		c = l-n
		i = 0
		while c:
			if i==k:
				i=0
			A[i]-=1
			i+=1
			c-=1

	# print(A)
	prod = 1
	for x in A:
		prod=(prod* (x**2 - x))%1000000007
	return prod 

while t:
	n,k = [int(x) for x in input().split()]
	print(cal(n,k))

	t-=1
