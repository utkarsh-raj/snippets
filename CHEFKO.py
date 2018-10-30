import heapq

for _ in range(int(input())):
	n, k = map(int, input().split())
	arr = []
	for i in range(n):
		arr.append(list(map(int, input().split())))
	arr.sort()
	he = []
	for i in range(k-1):
		heapq.heappush(he, arr[i][1])
	ans = 0
	for i in range(k-1,n):
		t = heapq.heappushpop(he, arr[i][1])
		ans = max(ans, 0, t-arr[i][0])
	print(ans)
