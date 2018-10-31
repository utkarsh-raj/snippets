arg = input()
for a in range(0, arg):
	b = map(int, raw_input().strip().split())
	list1 = map(int, raw_input().strip().split())

	list1.sort()
	list1.reverse()

	# list2 = list(set(list1))
	# list2.sort()
	# list2.reverse()

	kScore = list1[b[1] - 1]

	coun = 0
	for d in range(0, b[0]):
		if list1[d] >= kScore:
			coun += 1
	print coun
