'''
- 숫자를 적당히 더하고 빼서 타겟 넘버 만들기
1. 덧셈뺄셈은 순서가 상관이 없음
2. numbers를 기준으로 +- 확장해나가기
   (예) 4 - [+1, -1]
3. 리프노드의 값이 target인 개수 반환하기
4. 트리 ? dp ?
    4.1 dp - 2^n개
'''
def solution(numbers, target):    
    answer = 0
    dp = [[] for _ in range(len(numbers)+1)]
    dp[0] += [0]
    for i, n in enumerate(numbers):
        for prev in dp[i]:
            dp[i+1] += [prev+n, prev-n]
    answer = dp[-1].count(target)
    return answer