t=input()
for i in range(t):
	x,y,z=map(int,raw_input().split(" "))
	if y+z==x or x+y==z or x+z==y:
		print "yes"
	else:
		print "no
