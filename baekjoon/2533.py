'''
1. 얼리 아답터가 아닌 사람들은
 자신의 모든 친구들이 얼리 아답터일 때만 이 아이디어를 받아들인다. 
'''

import sys

N = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(N)]
for i in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u] += [v]
print(graph)