'''
1. 인접행렬으로 그래프 입력
2. 루트가 1일때의 리프노드들의 가중치합 구하기
    (예) 노드 9의 가중치합 = 28
3. 리프노드의 가중치합 중 가장 큰 가중치합을 가진 노드를 다시 루트로 설정
4. dfs 구현
    4.1 스택으로 구현했을 경우 -> 메모리 초과
        def dfs(root):
            stack = []
            visited = []

            # 각 노드까지의 경로합 저장
            dp = [0 for _ in range(n+1)]
            # 시작노드의 경로합 = 0
            dp[root] = 0

            stack.append(root)
            visited.append(root)

            while stack:        
                r = stack.pop()
                for c in range(n+1):
                    if tree[r][c] != 0 and c not in visited:
                        # to노드의 경로합 = from 노드의 경로합 + tree[from][to]
                        dp[c] = dp[r] + tree[r][c]
                        visited.append(c)
                        stack.append(c)
            return dp

    4.2 재귀함수로 구현 -> 메모리초과
        ㄴ 인접행렬로 구현 시, NxN 메모리
        =   => 트리 구현 방법 수정
'''
# SOLVED

import sys
sys.setrecursionlimit(10**9)

# 노드 개수
n = int(sys.stdin.readline().rstrip())

# 인접행렬 그래프 tree[from][to] = weight
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    p, c, w = map(int, sys.stdin.readline().split())
    tree[p].append([c, w])
    tree[c].append([p,w])

# 깊이우선탐색과 동일, 중간에 경로합 업데이트 코드 추가
def dfs(r, weight):
    for c in tree[r]:
        nxt, w = c
        if dp[nxt] == -1:
            dp[nxt] = weight + w
            dfs(nxt, weight + w)

# root = 1일 때 경로합이 최대인 노드 구하기
dp = [-1 for _ in range(n+1)]
dp[1] = 0
dfs(1, 0)
max_leaf = dp.index(max(dp))

# 위에서 구한 노드를 루트로 설정하여 경로합 최대인 값이 지름
dp = [-1 for _ in range(n+1)]
dp[max_leaf] = 0
dfs(max_leaf, 0)
print(max(dp))