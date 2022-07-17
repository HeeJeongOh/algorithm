# 단어(공백을 기준)별로 짝/홀수 인덱스를 판단
# 단어 사이에 공백이 1개 이상
def solution(s):
    answer = ''
    n = 0
    for letter in s:
        if letter == ' ':
            answer += ' '
            n = 0
        else:
            if n % 2 == 0:
                answer += letter.upper()
            else:
                answer += letter.lower()
            n += 1        
    return answer

print(solution('try hello world'))