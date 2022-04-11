'''
1. 인접행렬으로 그래프 입력
2. 루트가 1일때의 리프노드들의 가중치합 구하기
    (예) 노드 9의 가중치합 = 28
3. 리프노드의 가중치합 중 가장 큰 가중치합을 가진 노드를 다시 루트로 설정
'''

import sys

# 노드 개수
n = int(sys.stdin.readline().rstrip())

# 인접행렬 그래프 tree[from][to] = weight
tree = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(n-1):
    p, c, w = map(int, sys.stdin.readline().split())
    tree[p][c] = w
    tree[c][p] = w

# 깊이우선탐색과 동일, 중간에 경로합 업데이트 코드 추가
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

# root = 1일 때 경로합이 최대인 노드 구하기
get_leaf = dfs(1)
max_leaf = get_leaf.index(max(get_leaf))

# 위에서 구한 노드를 루트로 설정하여 경로합 최대인 값이 지름
d = max(dfs(max_leaf))
print(d)