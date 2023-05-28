'''
[시도1] 정확성(런타임에러1 시간초과 5) + 효율성(x)
1. n을 2진수로 변환
    1.1 나머지 이어붙이기
2. 1의 개수가 동일한 경우의 수 추출
    2.1 1의개수 0의 개수 조합하여 만들기
3. 10진수 변환 후, n보다 큰 수 중 가장 작은 수 선정

from itertools import permutations
import math

def toBinary(n):
    nstr = ''
    while n > 0:
        nstr += str(n % 2)
        n = (n - n%2) // 2
    return nstr[::-1]

def toTen(nstr):
    n = 0
    for i, s in enumerate(nstr[::-1]):
        if s == '1': 
            n += math.pow(2, i)
    return int(n)

def solution(n):
    nbin = toBinary(n)
    ones = nbin.count('1')
    
    if ones == len(nbin):
        tmp = nbin[0] + '0' + nbin[1:]
        return toTen(tmp)
    
    tmp = ['0' for _ in range(len(nbin) - ones)] + ['1' for _ in range(ones-1)]
                                                    
    nums = []
    for c in list(set(permutations(tmp))):
        a = '1'+"".join(c)
        nten = toTen(a)
        if nten > n:
            nums.append(nten)
    return min(nums)

[시도2]
0. 런타임에러 - 1 예상
1. 2진수, 10진수 변환 라이브러리 사용 -> 동일 결과
2. 1의 개수가 동일한 경우의 수
    2.1 숫자를 1 씩 늘려가며 이진수 변환하여 1개수 세기

def solution(n):
    if n == 1:
        return 2

    nbin = bin(n)[2:]
    one = nbin.count('1')
    if nbin == '1'*one:
        tmp = nbin[0] + '0' + nbin[1:]
        return int(tmp, 2)    
    
		# 10보다 크지 않을 것으로 임의의로 테스트하다가 얻어걸림 -> 다른사람 풀이 확인하니 while로 해도 됨
    for num in range(n+1, n+11):
        nbin = bin(num)[2:]
        ones = nbin.count('1')
        
        if ones == one:
            return num

            
[다른사람풀이] : 해당 코드에 모든 경우의 수 포함됨
'''
def solution(n):
    one = bin(n).count('1')

    for num in range(n+1, n+11):
        nbin = bin(num)[2:]
        ones = nbin.count('1')
        
        if ones == one:
            return num
