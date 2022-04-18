'''
1. value의 음수값을 우선순위로 설정
    ㄴ (우선순위, 값)
2. heapq 자체가 min heap임을 활용
'''
import sys
import heapq

heap = []
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    if num != 0:
        heapq.heappush(heap, (-num, num))
    else:
        if not heap:
            print(0)
            continue
        print(heapq.heappop(heap)[1])
