'''
1. 컴퓨터 = 노드
2. 노드의 개수를 입력받고 2차워배열 통해 그래프 생성
3. 2차원배열의 값이 1인 경우, 연결되어 있음
4. 그래프 순회를 통해 cnt++
    > 1차시도 : 시간초과
        while(True):
            if len(tmp) == 0:
                break
            next = tmp.pop()
            for j in range(n+1):
                if graph[next][j] == 1 and tmp.__contains__(j) == False:
                    tmp.append(j)
                    cnt += 1
    > 2차시도 : 성공 
        for i in tmp:    
            # print(i, tmp)
            for j in range(2, n+1):
                if graph[i][j] ==1 and not tmp.__contains__(j):
                    tmp.append(j)
                    cnt += 1
'''
# SOLVED

import sys

n = int(sys.stdin.readline().rstrip())
e = int(sys.stdin.readline().rstrip())

# nxn 2차원 배열 생성
graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
tmp = []
cnt = 0

for _ in range(e):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1
    if a == 1:
        tmp.append(b)
        cnt += 1

for i in tmp:    
    # print(i, tmp)
    for j in range(2, n+1):
        if graph[i][j] ==1 and not tmp.__contains__(j):
            tmp.append(j)
            cnt += 1
print(cnt)

