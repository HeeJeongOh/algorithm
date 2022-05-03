''''
1. 새로운 값이 들어올 때마다 정렬(sorted) -> 시간초과
    1.1 홀수일 경우 : nums[len(nums)//2
    1.2 짝수일 경우 : nums[len(nums)//2 - 1
2. heapq(우선순위큐) 활용 -> 시간초과
    2.1 min(nums[len(nums)//2][1], nums[len(nums)//2 + 1][1])
3. heap 두 개 사용 <힌트>
    3.1 힙 -> 최대, 최소, 힙의 크기
    3.2 

'''

import sys
import heapq

N = int(sys.stdin.readline().rstrip())

min_heap = []
max_heap = []
for i in range(N):
    n = int(sys.stdin.readline().rstrip())

    heapq.heappush(min_heap, (n, n))
    heapq.heappush(max_heap, (-n, n))

    print(min_heap)
    print(max_heap)