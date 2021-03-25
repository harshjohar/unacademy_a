n, m = map(int, input().split())

ans_key = input().split()
ans_key = str(ans_key)

for i in range(n):
	count = 0
	response = input().split()
	for j in range(m):
		response[j] = list(response[j])
		response[j].sort()
		

	for k in range(m):
		if response[k] == ans_key[k]:
			count+=1

	print(count)