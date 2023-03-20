'''
- 각 원소의 합 = s
- 각 원소의 곱 최대인 조합 찾기
1. a + b + c = S :: n+s-1 H s 의 해 찾기
2. 최대 값들이 가까울 때
3. 구글링 힌트 참고함. 
'''
def solution(n, s):
    answer = []
    if n == 1:
        return [s]
    if s // n == 0:
        return [-1]
    
    nums = []
    for _ in range(n):
        nums.append(s // n)
        s = s - (s//n)
        n -= 1
    return nums