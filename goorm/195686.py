'''
1. max값을 기준으로 split
2. 좌우 각각이 sorted결과와 동일한지 비교
3. 문제 없을 경우 sum 반환
'''
def solution(N, tastes):
	tmax = tastes.index(max(tastes))
	small = tastes[:tmax]
	large = tastes[tmax+1:]
	
	if sorted(small) == small and sorted(large, reverse=True) == large:
		return sum(tastes)
	else:
		return 0


N = int(input())
tastes = list(map(int, input().split()))
print(solution(N, tastes))
