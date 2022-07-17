'''
1. VxV 크기의 2차원 배열 생성 후 가중치 값 입력받기
2. s노드 -> i노드 최단경로 값 구하기 - 함수
    2.1 각 i노드에 대한 최단경로 값을 저장할 리스트
        - s노드의 최단경로 값은 항상 0
    2.2 shortestPath 구하는 함수
        - s와 직접 연결
        - s와 간접 연결
'''
# UNSOLVED

from collections import deque
import sys

V, E = map(int, sys.stdin.readline().split())
S = int(sys.stdin.readline().rstrip()) - 1

graph = [[]for _ in range(V)]   
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u-1].append((v-1, w))
print(graph)

dist = [-1 for _ in range(V)]
dist[S] = 0

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    q =  (0, start)
    dist[start] = 0

    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(S)

for out in dist:
    if out == -1:
        print("INF")
    else:
        print(out)
