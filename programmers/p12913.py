'''
1. 시작점을 달리하여 for문수행
2. 매 줄마다 연속된 열이 아닌 값들 중 최댓값 선택
    2.1 확신은 없는데 다른 방안이 안 떠오름

def solution(land):
    answer = []
    for start in range(4):
        total = land[0][start]
        before = start
        test = [total]
        for i in range(1, len(land)):
            tmp = land[i].copy()
            tmp[before] = 0
            
            nmax = max(tmp)
            nidx = tmp.index(nmax)
            
            before = nidx
            total += nmax
            
            test += [nmax]
        # print(test, total)
        answer += [total]
                
    return max(answer)
'''
'''
[다른사람풀이]
| 1 | 2 | 3 | 5 |
| 5 | 6 | 7 | 8 |
| 4 | 3 | 2 | 1 |
'''
def solution(land):
    for i in range(1,len(land)):
        land[i][0] = max(land[i][0]+land[i-1][1], land[i][0]+land[i-1][2], land[i][0]+land[i-1][3])
        land[i][1] = max(land[i][1]+land[i-1][0],land[i][1]+land[i-1][2],land[i][1]+land[i-1][3])
        land[i][2] = max(land[i][2]+land[i-1][0],land[i][2]+land[i-1][1],land[i][2]+land[i-1][3])
        land[i][3] = max(land[i][3]+land[i-1][0],land[i][3]+land[i-1][1],land[i][3]+land[i-1][2])

    return max(land[i])
