from collections import deque
import sys

N, M, R = map(int, sys.stdin.readline().split())

E = {i: [] for i in range(N+1)}
visited = [0 for i in range(N+1)]
rank = [0 for _ in range(N+1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    # 무방향
    E[a].append(b)    
    E[b].append(a)

# 문제조건에서 작은 숫자 먼저 방문해야하기 때문
for i in range(N):
    E[i] = sorted(E[i])

### bfs ###
q = deque()

# 시작정점 관련 정보 저장
q.append(R)
visited[R] = 1
rank[R] = 1

cnt = 2
while q:
    u = q.popleft()
    for v in E[u]:
        if visited[v] == 0:
            visited[v] = 1
            q.append(v)
            rank[v] = cnt
            cnt += 1

# output
for i in range(1, N+1):
    print(rank[i])


