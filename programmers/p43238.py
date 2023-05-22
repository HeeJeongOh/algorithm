'''
[시도1]
1. 구조 새롭게 tmp = [(우선순위 값, 인덱스), ...]
    1.1 list sort -> test2 통과 x, 문제 의도와 다름
    1.2 heap maxheap
    1.3 queue deque
'''
from collections import deque

def solution(priorities, location):
    q = []
    for idx, p in enumerate(priorities):
        q.append((p, idx))
    cnt = 0
    while True:
        maxp, _ = max(q)
        p, idx = q.pop(0)
        if p < maxp:
            q.append((p, idx))
        else:
            cnt += 1
            if idx == location:
                return cnt
    return -1