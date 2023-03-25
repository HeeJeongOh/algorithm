'''
t에서 p와 길이 같은 문자열 중, p가 나타내는 수보다 작거나 같은 것이 나오는횟수
1. p 길이를 가지고 있는 문자열 추출 -> slicing
2. 비교 후, cnt += 1

(+) num, p 자료형을 맞춰주어야 비교 가능.
'''
def solution(t, p):
    cnt = 0
    l = len(p)
    for i in range(len(t)-l+1):
        num = t[i:i+l]
        if num <= p:
            cnt += 1    
    return cnt