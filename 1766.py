import sys

def f2(x):
    return x[1]
N, M = map(int, sys.stdin.readline().split())
heap = {}
for i in range(1, N+1):
    heap[i] = i

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    heap[b] += heap[a]
heap = sorted(heap.items(), key=f2)

for i in heap:
    print(i[0], end=" ")