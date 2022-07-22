### 예제 통과 -> 테스트 실패
def solution(s, n):
    answer = ''
    wrd = list(s)
    for i in range(len(wrd)):
        if wrd[i] == " ":
            answer += " "
        elif wrd[i] == "z" or wrd[i] == "Z":
            answer += chr(ord(wrd[i])-26 + n)
        else:
            answer += chr(ord(wrd[i]) + n)
    return answer

print(solution("AaZz", 25))
print(solution("a     b", 1))
print(solution("a b ", 1))

