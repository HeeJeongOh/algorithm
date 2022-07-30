# 단어(공백을 기준)별로 짝/홀수 인덱스를 판단
# 단어 사이에 공백이 1개 이상
def solution(s):
    answer = ''
    cnt = 0
    for l in s:
        if l == ' ':
            answer += ' '
            cnt = 0
        else:
            if cnt % 2 == 0:
                answer += l.upper()
            else:
                answer += l.lower()
            cnt += 1
    return answer

print(solution('try hello world'))