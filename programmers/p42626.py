# sorted 활용 시 '시간초과'
# heapq 활용하여 자동 정렬
from heapq import heapify, heappush, heappop

def solution(scoville, K):
    ans = 0
    heapify(scoville)
    
    while True:                 
        first = heappop(scoville) 

        if first >= K:
            break
        # 첫 시도 런타임 에러 원인 - 예외 설정
        if len(scoville) == 0:
            return -1
            
        second = heappop(scoville)
        mix = first + (second*2)        
        heappush(scoville, mix)        
        ans += 1         
        
    return ans