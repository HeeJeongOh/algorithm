'''
1. 시간초과
    1.1 조합이 9가 되는 경우 모두 찾기
        ㄴ nCn, nCn-1, nCn-2, ... , nC1
    1.2 nCr의 합 <= 9가 될 경우, break
2. 
    2.1
'''

# 부서 별 신청한 금액
d = [1, 3, 2, 5, 4]
budget = 9

from itertools import combinations

def solution(d, budget):
    answer = 0

    for i in range(len(d), 0, -1):
        combs = list(combinations(d, i))
        print(i, combs)
        for c in combs:
            if sum(c) <= budget:
                answer = i
                return answer
    return answer

print(solution(d, budget))