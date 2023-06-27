'''
[시도1] 47.4 / 100.0
1. 공통인 수 찾기
    1.1 set을 이용해서 숫자 종류 파악
    1.2 공통인 숫자 개수만큼 늘리기
2. 찾은 수들을 내림차순 정렬하여 문자열로 반환

[시도2]
ㄴ answer을 문자열 형태로 유지 - int형 범위 유지 목적
ㄴ 반례 : "1000000002", "20200", => "2000"
'''
def solution(X, Y):
    inter = list(set(X).intersection(set(Y)))
    if inter == []:
        return '-1'

    answer = ''
    inter.sort(reverse=True)
    for i in inter:
        answer += i * min(X.count(i), Y.count(i))
        
    return "0" if answer == '0' * len(answer) else answer