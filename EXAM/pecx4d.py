def solve(n):
	global count

	if n == 1:
		count+=1
		return

	if n%2 == 0:
		solve(n-1)
		solve(n/2)
	if n%2 != 0:
		solve(n-1)

	return

count = 0
n = int(input())
solve(n)
print(count)