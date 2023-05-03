'''
[시도1] 런타임에러
1. answer += (word[0].upper() + word[1:].lower())
[시도2]
1. 한 글자 단어에 대해 예외처리 수행

(+)
- str.title() : 문자열 내 띄어쓰기 기준으로 각 단어의 첫글자는 대문자로, 나머지는 소문자로 변환
    # 첫 문자를 대문자로 - 3people -> 3People
    def solution(s):
         return s.title()

- str.capitalize() : 문자열 내 첫 글자를 대문자로 변환
    def solution(s):
         return ' '.join([word.capitalize() for word in s.split(" ")])
'''
def solution(s):
    answer = ''
    for word in s.split(" "):
        if len(word) > 1:
            answer += (word[0].upper() + word[1:].lower())
        else:
            answer += word.upper()
        answer += " "
    
    return answer[:-1]
