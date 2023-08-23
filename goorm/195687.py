'''
1. 10진수 => [10진수, 1의 개수]
2. x[1], x[0]에 대해 정렬
'''
def solution(N, K, nums):
	ans = [[nums[i], bin(nums[i]).count('1')] for i in range(N)]
	ans.sort(key=lambda x: (x[1], x[0]), reverse=True)
	return ans[K-1][0]

N, K = map(int, input().split())
nums = list(map(int, input().split()))
print(solution(N, K, nums))
