# int(n**1/2)+1 -> 시간초과
# int(n**(1/2)+1) -> 통과
# ㄴ 괄호를 넣지 않아 오해 발생
def is_prime(n):
    for i in range(2, int(n**1/2)+1):
        if n % i == 0:
            return False
    return True

def solution(n):
    answer = 0
    for i in range(2, n+1):
        if is_prime(i):
            answer += 1
    return answer