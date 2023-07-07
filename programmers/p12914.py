'''
[시도1] 실패 1 시간초과 11 
0. 1과 2를 이용하여 n을 만드는 경우의 수
1. 같은 것이 있는 순열 활용하기
    1.1 2가 들어갈 위치 고르기
2. 2의 개수를 이용하여 조합 구성 

from itertools import combinations

def solution(n):
    answer = 0
    for i in range((n//2), -1, -1):
        twos = [2 for _ in range(i)]
        ones = [1 for _ in range(n - sum(twos))]
        items = ones + twos

        answer += len(list(combinations(items, i)))
        
    return answer

[시도2] 시간초과 12
1. 트리 형태로 계산하기 (타겟넘버)
2. dp[i] 갱신하는 부분에서 n보다 큰 경우 제거하기

def solution(n):    
    if n == 1:
        return 1
    
    if n == 2:
        return 2
    
    answer = 0
    dp = [[] for _ in range(n)]
    dp[0] += [1, 2]
    
    for i in range(1, n):
        for prev in dp[i-1]:
						if prev == n:
								answer += 1
								answer = answer % 1234567
						# prev+2 조건 추가 후 분리해도 동일 결과
            if prev+1 <= n:
                dp[i] += [prev+1, prev+2]
        # print(dp[i])
        # answer += (dp[i].count(n)) % 1234567
        
    return answer % 1234567
'''
'''
[시도3] 질문하기 참고
1. 순열 이용
2. 피보나치 규칙 발견하기 = dp
	2.1 귀납적으로 생각하기 : n칸까지 뛰는 방법 = [n-1]칸 + 1칸 + [n-2]칸 + 2칸
'''
# 1번
from itertools import permutations
def solution(n):
    answer = 0
    facts = [1, ]
    
    # facts : n! 값 저장
    for i in range(1, n+1):
        facts.append(facts[-1] * i)
    
    # 1의 개수 : 홀수인 경우, 홀수 개.필요
    one = 0 if n % 2 == 0 else 1
    # 2의 개수 : n // 2 ~ 0 의 개수를 가질 수 있음
    for two in range(n // 2, -1, -1):
        answer += facts[two + one] // (facts[two] * facts[one])
        one += 2

    return answer % 1234567