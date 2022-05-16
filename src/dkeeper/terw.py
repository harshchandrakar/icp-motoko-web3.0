def LongestSubsetWithZeroSum(arr):
	s = 0
	checker = {}
	maxLen = 0
	for i in range(len(arr)):
		s+=arr[i]
		if s not in checker:
			checker[s] = i
		else:
			maxLen = max(maxLen,i-checker[s])
	return maxLen

arr = [1 ,3 ,-1, 4 ,-4]
print(LongestSubsetWithZeroSum(arr))