'''
1. 조건이 주어진 경우, 우선순위값 수정 -> 틀렸습니다.
    1.1 a가 b보다 먼저 풀어야한다 -> heap[b] += heap[a]
2. 위상정렬 - 스태 / 큐 <힌트>
    ㄴ 선수조건이 있는 경우 활용
    2.1 진입차수가 0인 정점 큐에 삽입
    2.2 큐에서 원소를 꺼내 연결된 간선 제거
    2.3 진입차수가 0인 정점 큐 삽입
3. 가능하면 쉬운 문제부터 풀어야한다. -> 큐 삽입 시, 우선순위 따지기
'''
# SOLVED

import sys
import heapq

N, M = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(N + 1)]
degree = [0 for _ in range(N+1)]

for i in range(M):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    graph[A].append(B)
    degree[B] += 1

# heapq를 활용해서 '가능하면 쉬운문제부터' 조건 만족
q = []
for i in range(1, N + 1):
    if degree[i] == 0:
        heapq.heappush(q, i)

result = []
while q:
    tmp = heapq.heappop(q)
    result.append(tmp)
    for i in graph[tmp]:
        degree[i] -= 1
        if degree[i] == 0:
            heapq.heappush(q, i)

print(" ".join(map(str, result)))