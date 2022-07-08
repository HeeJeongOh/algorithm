'''
https://school.programmers.co.kr/learn/courses/30/lessons/12977
1. nums에 있는 숫자들 중 3개의 합 리스트를 구하기
2. 해당 리스트 값들 중 소수 판별하기
'''

nums = [1,2,3,4]

import math
from itertools import combinations

def is_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if (n%i) == 0:
            return False
    return True


def solution(nums):
    answer = 0
    combs = list(combinations(nums, 3))
    for a, b, c in combs:
        if is_prime(a+b+c):
            answer += 1
    return answer

print(solution(nums))
