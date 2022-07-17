''''
1. 새로운 값이 들어올 때마다 정렬(sorted) -> 시간초과
    1.1 홀수일 경우 : nums[len(nums)//2
    1.2 짝수일 경우 : nums[len(nums)//2 - 1
2. heapq(우선순위큐) 활용 -> 시간초과
    2.1 min(nums[len(nums)//2][1], nums[len(nums)//2 + 1][1])
3. heap 두 개 사용 <힌트: https://art-coding3.tistory.com/44>
    3.1 left heap : 중간값보다 작은 수 입력 <max_heap>
        ㄴ 해당 힙의 루트 = 중간값
    3.2 right heap : 중간값보다 큰 수 입력 <min_heap>
'''

# UNSOLVED

import sys
import heapq

N = int(sys.stdin.readline().rstrip())

left_heap = []
right_heap = []
result = []

for i in range(N):
    n = int(sys.stdin.readline().rstrip())

    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, (-n, n))
    else:
        heapq.heappush(right_heap, (n, n))

    # right가 empty하지 않고
    if right_heap:
    
        # left의 root(최댓값)과 right의 root(최솟값) 비교
        if left_heap[0][1] > right_heap[0][1]:

            # 
            max = heapq.heappop(left_heap)[1]
            min = heapq.heappop(right_heap)[1]

            heapq.heappush(left_heap, (-min, min))
            heapq.heappush(right_heap, (-max, max))

    result.append(left_heap[0][1])


for r in result:
    print(r)