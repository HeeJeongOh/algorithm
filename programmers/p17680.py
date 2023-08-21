'''
[시도1] 80.0 / 100.0 : 실패 4
1. 최소 사용 도시 지우기
2. cacheSize길이만큼 리스트 생성
'''
def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities)*5
    
    cities = [c.lower() for c in cities]
        
    answer = cacheSize*5
    q = cities[:cacheSize]
    
    for c in cities[cacheSize:]:
        print(c, q)
        if c in q:
            answer += 1
            q.remove(c)
        else:
            answer += 5
            q.pop(0)
        q += [c]
        
    return answer


'''
[다른사람풀이] - 알고리즘은 동일
ㄴ q에 있는 경우 q.pop(0) 을 안하고 자료형을 deque를 사용했더니 알아서 앞에거 사라짐
ㄴ 그래도 되어야하는데 차이를 모르겠음
'''
from collections import deque

def solution(cacheSize, cities):
    dq = deque(maxlen=cacheSize)
    run_time = 0
    for city in cities:
        city = city.lower()
        if city not in dq: # cache miss
            dq.append(city)
            run_time += 5
        else: # cache hit
            dq.remove(city)
            dq.append(city)
            run_time += 1

    return run_time