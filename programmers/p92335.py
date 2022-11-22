import math

def isPrime(x):
    if x == 1:
        return False
    for i in range (2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True
                    
def solution(n, k):
    answer = 0
    nnum = ''
    # k진수 변환
    while n > 0:
        nnum += str(n % k)
        n = n // k
    nums = nnum[::-1].split('0')    
    print(nums)

    for n in nums:
        if n == '':
            continue
        if isPrime(int(n)):
            print(n)
            answer += 1
    
    return answer

print(solution(437674, 3))