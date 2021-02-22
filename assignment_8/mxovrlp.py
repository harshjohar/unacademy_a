t = int(input())
for _ in range(t):
	n = int(input())
	m = int(input())
	ongoing_classes = {}
	times = []
	for i in range(n):
		s, e = map(int, input().split())
		if s in ongoing_classes:
			ongoing_classes[s]+=1
		else:
			ongoing_classes[s]=1
			times.append(s)
		if e+1 in ongoing_classes:
			ongoing_classes[e+1]-=1
		else:
			times.append(e+1)
			ongoing_classes[e+1]=-1
	times.sort()
	result = 0
	sum_class = 0
	for i in times:
		sum_class += ongoing_classes[i]
		result = max(result, sum_class)
	print(result)