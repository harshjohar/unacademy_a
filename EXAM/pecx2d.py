def solve(x,y):
	global count
	global n, m

	if x == n or y == m:
		count += 1
		return

	if x+1 >= y:
		solve(x+1, y)

	if x >= y+1:
		solve(x, y+1)

	return  


for _ in range(int(input())):
	n, m = map(int, input().split())
	count = 0
	solve(1, 1)
	print(count)