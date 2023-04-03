''''
[시도1] 시간초과 28/34
1. tangerine 크기 별 갯수 세기 -> defaultdict, count
    for t in set(tangerine):
        dd[t] = tangerine.count(t)
    dd = sorted(dd.items(), key=lambda x:x[1], reverse=True)
2. value로 정렬하여 k에 따라 최소 종류 세기
    sum += dd[t]
    sum > dd[t] : return cnt
    
[시도2] 시간초과 28/34
1. 어떤 귤인지 파악할 필요 없이 개수와 종류만 기억하면 됌 -> count, dd = []
2. 정렬이 아닌 max값만 추출하기 -> max

[시도3] 성공
1. set, count 사용 X
'''

def solution(k, tangerine):
    tcnt = {t: 0 for t in tangerine}
    for t in tangerine:
        tcnt[t] += 1
    
    tcnt = sorted(tcnt.items(), key=lambda x: x[1], reverse=True)

    total = 0
    for i, (_, t) in enumerate(tcnt):
        total += t
        if total >= k:
            return i+1
            
    return 0