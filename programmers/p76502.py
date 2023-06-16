'''
[시도1] : 85.7 / 100.0
1. 왼쪽으로 한칸씩 움직이기
    1.1 for 문이 끝나도록 올바른 괄호문자열 안나오면 -1
2. 올바른 괄호 문자열인지 확인하기
    3.1 stack = [[][][]]
    3.2 if 문 6개로 처리
[시도2]
- 테13 반례 "({["  -> 마지막에 남은 stack 확인
[시도3]
- if문 6개 -> 딕셔너리 이용
- 테14 반례 "{(})"
    이전 것이 열린괄호면 열린괄호거나 그에 해당하는 닫힌괄호가 나와야 함
    -> 이전 괄호 저장했다가 비교
'''
d = {'(': 0, ')': 0, '[': 1, ']': 1, '{': 2, '}': 2}
def check(s):
    stack = [[],[], []]
    before = ''
    for v in s:
        if v in ['(', '[', '{']:
            stack[d[v]].append(v)
            before = v
        else:
            # 테스트 14
            if before != '' and d[before] != d[v]:
                return False
            # 인덱스에러 처리
            try:
                stack[d[v]].pop()
            except:
                return False
            before = ''

    # 테스트 13
    if stack[0] or stack[1] or stack[2]:
        return False
    
    return True        
    
def solution(s):
    answer = 0
    for i in range(len(s)):
        tmp = s[i:] + s[:i]
        if check(tmp):
            answer += 1
    return answer