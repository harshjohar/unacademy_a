'''
Farmers has a long barn with N stalls. The stalls are located along a straight line
0<=x<= 1e9
his C cows dont like this barn layout,
and become aggressive towards each other once put into stall. 
To prevent the cows from hurting each other, 
Farmer wants to assign the cows to the stalls, 
such that min distance between any two of them is as large as possible.
What is the largest minimum distance

Input
t = no. of test cases
line 1 : two integers, N and C
line 2-n+1 : line i+1 contains an integer stall location xi

Output:
For each test case output largest minimum distance
'''

# Minimax problem:
#	maximum of minimum
# max part : binary search
# min part : good function

def good(mid, barn, cows):
	count = 0
	last_pos = barn[0]
	for i in range(1, len(barn)):
		if barn[i] - last_pos >= mid:
			count+=1
			last_pos = barn[i]
		if count>=cows:
			return True

	return False
 

t = int(input())
for _ in range(n):
	n, c = map(int, input().split())
	barn = []
	for i in range(n):
		x = int(input())
		barn.append(x)

	barn.sort()
	lo = 1
	hi = barn[len(barn)-1]
	ans = -1
	while lo<=hi:
		mid = (lo+hi)//2
		if good(mid, barn, c):
			ans = mid
			lo = mid+1
		else:
			hi = mid-1