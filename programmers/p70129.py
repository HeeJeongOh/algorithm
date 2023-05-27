'''
1. x의 0 제거 - replace
2. x의 길이를 2진수로 변환 - bin
'''
def solution(s):
    cnt, zero = 0, 0

    while True:
        if int(s) == 1:
            break
        before = len(s)
        s = s.replace('0','')
        
        after = len(s)
        s = bin(after)[2:]
        
        zero += before-after
        cnt += 1
        
    return [cnt, zero]

'''
[다른사람풀이]: 굳이 s를 변화하지 않아도 됌. 1의 개수(전체길이-'0'의개수)만 구하기
'''
def solution(s):
    cnt, zero = 0, 0

    while True:
        if int(s) == 1:
            break
            
        zero += s.count('0')
        cnt += 1

        after = s.count('1')
        s = bin(after)[2:]
        
    return [cnt, zero]