'''
1. 문자열을 3개의 부분문자열로 나누기
	1.1 칸막이를 뽑는 개념으로 생각 : 인덱스 중 2개 선택, 0, N 제외
2. 중복 제거 후 사전 순서로 정렬 -> 점수 = (인덱스+1)
	2.1 map : ('부분문자열': (인덱스+1))
3. 각 부분 문자열에 대한 점수 계산 후 최대 점수 반환
'''
from itertools import combinations
def solution(N, S):
	# 1번
	blocks = combinations(range(1,N), 2)
	wlist, wset = list(), set()
	
	# 부분조합, 각각의 요소 저장
	for b1, b2 in blocks:
		wlist += [[S[:b1], S[b1:b2], S[b2:]]]
		wset.update([S[:b1], S[b1:b2], S[b2:]])
	
	# 2번
	wlist2 = sorted(list(wset))
	d = {w: i+1 for i, w in enumerate(wlist2)}
	
	# 3번
	answer = []
	for x, y, z in wlist:
		answer += [d[x] + d[y] + d[z]]
	
	return max(answer)

N = int(input())
S = input()
print(solution(N, S))
