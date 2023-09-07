'''
[시도1] 시간초과 + 런타임에러
1. 컴포넌트 만들기
2. 각 컴포넌트들의 밀도 구하기
	2.1 컴포넌트 내 통신회선 구하기 - 그래프 탐색 시 (a, b) 관계 저장 ?
	2.2 최종 답안에 (밀도, 컴포넌트 구성)
[시도2] 실패 + 시간초과
1. search(list) -> search(dict)
[시도3] 실패 7
1. 같은 밀도에 대한 조건 추가
'''
from collections import defaultdict

def solution(N, M, lines):
	# print(lines)
	visited = [0 for _ in range(N+1)]
	search = defaultdict(list)
	for i in range(1, N+1):
		if visited[i] == 0:
			visited[i] = 1
			q = lines[i]
			tmp = set([i])
			while q:
				n = q.pop()
				if visited[n] == 0:
					visited[n] = 1
					q += lines[n]
					tmp.add(n)
		
			cnt = set()				
			for t in tmp:
				for tt in lines[t]:
					cnt.add((min(t, tt), max(t, tt)))
			search[len(cnt)/ len(tmp)] += [sorted(tmp)]
			# print(cnt, tmp)
	# print(search)	
	return (' '.join(str(s) for s in search[max(search)][0]))


N, M = map(int, input().split())
lines = {i: [] for i in range(1, N+1)}
for a, b in [list(map(int, input().split()))for _ in range(M)]:
	lines[a] += [b]
	lines[b] += [a]
print(solution(N, M, lines))