'''
0. K칸 K 소비 / 현재칸x2 0 소비
1. 아무생각 없이 거꾸로 계산해서 결과 확인하니 꽤 많이 통과함(?)
'''
def solution(n):
    ans = 0
    while n > 0:
        if n % 2 == 0:
            n = n // 2
        else:
            ans += 1
            n -= 1
            
    return ans