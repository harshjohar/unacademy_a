# returns a binary string which tells a number in prime or not
# 1 means prime, 0 means not prime
def sieve(n):
	# index in the returning array tells the number
	prime = [1 for i in range(n+1)]
	prime[0], prime[1] = 0, 0
	p = 2
	while p*p <=n:
		if prime[p] == 1:
			for i in range(p*p, n+1, p):
				prime[i] = 0
		p+=1
	# print(prime)
	ans = []
	for i in range(len(prime)):
		if prime[i]==1:
			ans.append(i)
	return ans

t = int(input())
all_primes = sieve(10000)
for _ in range(t):
	n = int(input())
	# print(all_primes)
	mil_gya = False
	for i in range(len(all_primes)):
		if n-all_primes[i] in all_primes:
			print(all_primes[i], n-all_primes[i])
			mil_gya = True
			break
	if not mil_gya:
		print('-1 -1')