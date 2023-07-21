'''
1. 나타났던 문자에 대해 기록하기
2. 간격을 기억해야하니까 문자 + 인덱스 정보 저장
'''
from collections import defaultdict
def solution(s):
    answer = []
    records = defaultdict()
    for idx, letter in enumerate(s):
        if letter in records:
            answer += [idx - records[letter]]
        else:
            answer += [-1] 
        records[letter] = idx
    # print(records)
    return answer