'''
1. 우선순위 큐 : 계속해서 정렬해가며 넣기 -> 힙 ?
[시도1]
    일단 for, if, max, min, remove 쓰면 답안은 통과했으나 효율성에서 시간초과가 될 것 같음.
[시도2] 
    heapq 활용해보기 - 기본 min-heap
    ㄴ 주의 : 오름차순 정렬과는 다름. 마지막 값이 항상 최댓값 보장 x

*** 문제의도는 minheap과 maxheap을 같이 쓰는 것. 
'''
from heapq import heappush, heappop
# 3 - 최대한 코드 길이 줄여보기
def solution(operations):
    q = []
    for op in operations:
        if op[0] == "I":
            heappush(q, int(op[2:]))
        elif len(q) > 0:
            if op == "D 1":   
                q.pop(-1)   
            elif op == "D -1":
                heappop(q)
    return [0, 0] if len(q) == 0 else [max(q), q[0]]
    
# 2
def solution2(operations):
    q = []
    for op in operations:
        cm, num = op[0], int(op[2:])
        if cm == 'I':
            heappush(q, num)
        if cm == 'D' and len(q) > 0:
            if num == 1:
                q.pop(-1)
            elif num == -1:   
                q.pop(0)
        print(q)
    if len(q) == 0:
        return [0, 0]
    else:
        return [max(q), q[0]]
    
# 1
def solution1(operations):
    q = []
    for op in operations:
        cm, num = op[0], int(op[2:])
        if cm == 'I':
            q.append(num)
        if cm == 'D' and len(q) > 0:
            if num == 1:
                q.remove(max(q))
            elif num == -1:   
                q.remove(min(q))
        # print(q)
        
    if len(q) == 0:
        return [0, 0]
    else:
        return [max(q), min(q)]