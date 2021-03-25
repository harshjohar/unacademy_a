def subsets(li):
	ans = [[]]

	for i in range(len(li)):
		t = [ans[j][:] for j in range(len(ans))]
		n = li[i]

		for j in range(len(ans)):
			t[j].append(li[i])
		ans = ans + t

	return ans

print(subsets([1,2,3,4,5,6,7,8,12,13,4,5,2, 4, 3, 6, 7,8 ,5]))