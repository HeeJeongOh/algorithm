'''
1. 최소필요도 / 소모피로도
2. 완전탐색 키워드로 permutation 써서 모든 경우의 수 추출
'''
from itertools import permutations
def solution(k, d):
    answer = []
    tmp = list(permutations([i for i in range(len(d))]))
    for t in tmp:
        total = k
        cnt = 0
        for i in t:
            if total >= d[i][0]:
                total -= d[i][1]
                cnt += 1
            else:
                break
            answer.append(cnt)                
    return max(answer)