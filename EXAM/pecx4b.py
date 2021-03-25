def gcd(a, b):
	# euclid division lemma
	b = max(a, b)
	a = min(a, b)

	while a != 0:
		# print((a, b))
		tmp = b
		b = a
		a = tmp%a
	return b

for _ in range(int(input())):
	n = int(input())
	for i in range(1, n):
		if gcd(i, n) == 1:
			print(i)