'''
1. 빈 병 a개 => 콜라 b병
2. "단, 보유 중인 빈 병이 2개 미만이면, 콜라를 받을 수 없다"만 보고 풀어버림
    ㄴ 
'''
def solution(a, b, n):
    answer = 0
    while n >= a:
        cnt = n // a
        n -= cnt * (a-b)
        answer += cnt

    return answer * b