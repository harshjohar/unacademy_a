'''
Given number of pages of n different books & m is the value of no. of students.
Books are arranged in increasing order of pages.
One student can read consecutive books only.
Assign books such that max no. of pages assigned in minimum.

Input:
n = books
m = students

'''
def good(arr, s, mid):
	students_req = 1
	pages_read_by_curr = 0
	for i in range(len(arr)):
		if arr[i]>mid:
			return False
		if pages_read_by_curr+arr[i] > mid:
			students_req+=1
			pages_read_by_curr = arr[i]

			if students_req > s:
				return False	

		else:
			pages_read_by_curr+=arr[i]

	return True

def books(arr, s):
	lo = 0
	hi = sum(arr)
	ans = 10**9
	while lo<=hi:
		mid = lo+(hi-lo)//2
		if good(arr, s, mid):
			hi = mid-1
			ans = mid

		else:
			lo = mid+1
	return ans


arr = list(map(int, input().split()))
m = int(input())
print(books(arr, m))