'''
[시도1] 38.5 / 100.0
1. 반올림해서 가까운 숫자로 하면 되지 않을까
2. 2554 - 446 - 46 - 4

[시도2] 92.3 / 100.0
ㄴ (반례) 646 -> 13 : 646 - 650 - 700 - 1000
1. 반올림 방향성 2개(큰 자릿수, 작은 자릿수) 수행해보고 둘 중 작은 것 택하기

[시도3] 
ㄴ (힌트) 한 방향이 아니라 양방향으로 풀 것.
ㄴ https://school.programmers.co.kr/questions/41681
1.엘레베이터 -> 올라갈래 내려갈래
2. 나머지에 따라 경우의 수 나누기
    2.1 left < 5 -> 내려가기
    2.2 left > 5 -> 올라가기
    2.3 left = 5 이고 다음 숫자도 나머지가 5보다 크면 -> 올라가기
        ㄴ 어떻게 알았지...
'''
def solution(storey):
    answer = 0
    while storey != 0:
        n = storey % 10 
        if n > 5 or (n == 5 and (storey // 10) % 10 >= 5):
            storey += 10 - n
            answer += 10 - n
        else:
            answer += n

        storey = storey // 10

    return answer