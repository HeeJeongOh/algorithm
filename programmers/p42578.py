'''
[시도1] 28.6 / 100.0
1. 단독 착용인 경우
2. 타입1*타입2* ..  경우의 수
'''
from collections import defaultdict
def solution(clothes):
    answer = 0
    d = defaultdict(list)
    for cname, ctype in clothes:
        d[ctype].append(cname)
    
    comb = 1
    for ctypes in d:
        answer += len(d[ctypes])        
        comb *= len(d[ctypes])
        
    if len(d.keys()) > 1:
        answer += comb
        
    return answer

'''
[시도2] 96.4 / 100.0 : 테스트1 시간초과 
1. 단독 착용인 경우
2. 종류1 + 종류2 + 종류3 + 종류4
    2.1 종류1
    2.2 종류2 - 2가지 고르고 경우의 수 구하기
'''
from collections import defaultdict
from itertools import combinations

def solution(clothes):
    d = defaultdict(list)
    for cname, ctype in clothes:
        d[ctype].append(cname)
    
    answer = 0
    ntype = len(d.keys())
    for i in range(1, ntype+1):
        for types in combinations(d.keys(), i):
            # print(types)
            if len(types) == 1:
                answer += len(d[types[0]])
            else:
                tmp = 1
                for t in types:
                    tmp *= len(d[t])
                answer += tmp
            # print(answer)
    return answer

'''
[시도3] 질문하기 참고
1. (각 종류 별 개수+1) 곱 - 1 (아무것도 안 입는 경우)
'''
def solution(clothes):
    d = defaultdict(list)
    for cname, ctype in clothes:
        d[ctype].append(cname)
        
    answer = 1
    for ntype in d:
        answer *= (len(d[ntype])+1)
        
    
    return answer-1