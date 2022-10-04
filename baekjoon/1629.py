'''
!!! 분할정복 + 재귀함수 !!!
m**n = m**(n/2) * m**(n/2)     (n %2 == 0)
m**n = m**(n/2) * m**(n/2) * m (n%2 != 0)
'''
import sys

def calculate(m, n, k):

    if n == 0:
        return 1
    elif n == 1:
        return m % k

    tmp = calculate(m, n//2, k)

    if n % 2 == 0:
        return (tmp*tmp*m) % k
    else:
        return (tmp*tmp) % k


a, b, c = map(int, sys.stdin.readline().split())
print(calculate(a, b, c))