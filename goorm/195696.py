'''
[시도1]
1. 딕셔너리 형태로 그래프 생성
2. dfs 구성 - visited + queue
	2.1 q에 min 값만 넣기
	[시도2]
	2.2 양방향이기에 노드 값 모두 확인
'''
def solution(N, M, K, g):
	visited = [K]
	q = K
	for _ in range(N):
		# print(visited)
		if g[q] == []:
			break
		
		if set(visited).issubset(set(g[q])):
			break
		
		for tmp in sorted(g[q]):
			if tmp not in visited:
				visited += [tmp]
				q = tmp
				break
	return str(len(visited)) + ' ' + str(visited[-1])

N, M, K = map(int, input().split())
g = {n : [] for n in range(1, N+1)}
for _ in range(M):
	frm, to = input().split()
	g[int(frm)] += [int(to)]
	g[int(to)] += [int(frm)]
	
print(solution(N, M, K, g))