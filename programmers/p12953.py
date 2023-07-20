'''
이전 풀이
from math import gcd

# 최소공배수 = (a*b) // (a,b의 최대공약수)
def solution(arr):  
    ans = arr[0]
    for a in arr:
        ans *= (a // gcd(ans, a))    
    return ans

2 | 14 2 12
3 | 3 9  6
    -----
    1 3  2
[시도1]
ㄴ 전체 숫자들에게 공통된 약수를 찾으려고 했더니 반례 생김
    [2, 7, 14] - 14

def solution(arr):
    mnum = 1
    for i in range(2, max(arr)+1):
        flag = True
        for a in arr:
            if a % i != 0:
                flag = False
        if flag:
            mnum *= i
    # print(mnum)
    ans = mnum
    for a in arr:
        ans *= (a // mnum)

    return ans

[시도2]
ㄴ 힌트 참고 : 두 수 씩 계산
1. 최소공배수 구하여 갱신
'''
def lcm (a, b):
    lcm = 1;
    while True:
        if lcm % a == 0 and lcm % b == 0:
            break
        lcm += 1
    return lcm

def solution(arr):
    # 최소공배수 갱신하기
    a = arr[0]
    for b in arr[1:]:
        a = lcm(a, b)
    return a