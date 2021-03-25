def good(arr, n, p, mid):
	count = 0
	for i in range(0, n):
		alotted_time = mid
		paratas = 0
		time = arr[i]
		while alotted_time > 0:
			alotted_time -= time
			if alotted_time >= 0:
				paratas += 1
				time += arr[i]
		count += paratas
		if count >= p:
			return True
	return False

t = int(input())
for _ in range(t):
	order = int(input())
	chefs = list(map(int, input().split()))
	no_of_chefs = chefs[0]
	chefs.pop(0)

	lo = 0
	hi = int(1e7)
	ans = -1
	while lo<=hi:
		mid = lo+(hi-lo)//2
		if good(chefs, no_of_chefs, order, mid):
			hi = mid
			ans = mid

		else:
			lo = mid+1
		print(ans)
    