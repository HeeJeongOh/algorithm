from itertools import combinations
def solution(number):
    answer = 0
    # for c in combinations(number,3): 로 변경 가능
    comb = list(combinations(number, 3))
    for c in comb:
        if sum(c) == 0:
            answer += 1
    return answer