'''
1. 지도 2차원 배열에 값 저장
2. 2차원 배열에서 단지를 찾고, 단지 내 집의 수 찾기
    2.1 단지 찾기
        - vilage = []: 단지 내 집의 수 저장리스트
        - DFS(시작점) 후 완료하면 
        - 시작점에서 우측으로 이동해가면서 새로운 1 찾기
    2.2 단지 내 집 찾기 - DFS
        - visited : 방문한 집의 좌표
        - 상하좌우 순으로 탐색하기
3. 출력
    - 오름차순 정렬 : vilage.sort()
    - 단지 수 = len(vilage)
    - 단지 내 집의 수 = print(vilage[i])
'''

import sys

def DFS(r, c, visited):
    graph[r][c] = -1
    visited.append((r,c))
    
    if r != 0 and graph[r-1][c] == 1 and (r-1, c) not in visited:
            graph[r-1][c] = -1
            DFS(r-1, c, visited)

    if r != n-1 and graph[r+1][c] == 1 and (r+1, c) not in visited:
        graph[r+1][c] = -1
        DFS(r+1, c, visited)
        
    if c != 0 and graph[r][c-1] == 1 and (r, c-1) not in visited:
        graph[r][c-1] = -1
        DFS(r, c-1, visited)
    
    if c != n-1 and  graph[r][c+1] == 1 and (r, c+1) not in visited:
        graph[r][c+1] = -1
        DFS(r, c+1, visited)

    return visited

n = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n)]    
for i in range(n):
    graph[i] = list(map(int, sys.stdin.readline().rstrip()))

vilage = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            # DFS의 return 값 = 단지 내 집의 수
            vilage.append(len(DFS(i, j, [])))

vilage.sort()
print(len(vilage))
for v in vilage:
    print(v)


