'''
시도1 -> 시간초과
    1.1 x !=0 : 배열에 x 추가
    1.2 x == 0 : 가장 작은 값 출력, 제거
    for _ in range(n):
        num = int(sys.stdin.readline().rstrip())
    if num != 0:
        heap.append(num)
    else:
        if not heap:
            print(0)
            continue
        print(min(heap))
        heap.remove(min(heap))

시도2 -> 시간초과
    2.1 deque로 변경 + sort 활용
    for _ in range(n):
        num = int(sys.stdin.readline().rstrip())
    if num != 0:
        heap.append(num)
        heap = deque(sorted(heap))
    else:
        if not heap:
            print(0)
            continue
        print(heap.popleft())

시도3
    3.1 파이썬 heapq 자료구조 improt
    ㄴ heapq : 이진트리 기반의 최소 힙 ~~ JAVA - Priority Queue
    ㄴ https://www.daleseo.com/python-heapq/

'''
import sys
import heapq

heap = []
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    num = int(sys.stdin.readline().rstrip())
    if num != 0:
        heapq.heappush(heap, (i, num))
    else:
        if not heap:
            print(0)
            continue
        print(heapq.heappop(heap))

