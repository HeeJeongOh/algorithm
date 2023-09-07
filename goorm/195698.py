'''
1. 연합
	1.1 a-b, b-a 직접 연결
	1.2 ab 연합, bc 연합 -> ac 연합
2. 연합의 수
	2.1 양방향인 것들의 조합 찾기
	2.2 조합 중에 연결고리 찾아 합치기
		2.2.1 연합끼리 그래프 생성
	2.3 나머지 단독 연합 더하기
'''
from collections import defaultdict
def solution(N, M, islands):
	# print(islands)
	# 1
	group = set()
	for i in islands:
		for j in islands[i]:
			if i in islands[j]:
				group.add((min(i, j), max(i, j)))
	# print(group)
	# 2
	regroup = []
	mmap = defaultdict(list)
	for a, b in group:
		mmap[a] += [b]
		mmap[b] += [a]
	# print(mmap)
	visited = [0 for i in range(N+1)]
	for i in range(1, N+1):
		if visited[i] == 0:
			tmp = [i]
			visited[i] = 1
			q = mmap[i]
			
			while q:
				n = q.pop(0)
				if visited[n] == 0:
					tmp += [n]
					visited[n] = 1
					q += mmap[n]
			# print(n, q)
			regroup += [tmp]
	# print(regroup)
	return len(regroup)

N, M = map(int, input().split())
islands = {i: [] for i in range(1, N+1)}
for _ in range(M):
	frm, to = map(int, input().split())
	islands[frm] += [to]
print(solution(N, M, islands))