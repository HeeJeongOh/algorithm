### 예제 통과 -> 테스트 실패
# 반례 : solution("P", 15) => "E"
def solution(s, n):
    answer = ''
    wrd = list(s)
    for i in range(len(wrd)):
        if wrd[i] == " ":
            answer += " "
        else:
            # ord 순서 : A-Z a-z
            oo = ord(wrd[i])
            if (oo+n) > ord('Z') and oo <= ord('Z'):
                answer += chr(oo+(n-26))
            elif (oo+n) > ord('z') and oo <= ord('z'):
                answer += chr(oo+(n-26))
            else:
                answer += chr(ord(wrd[i])+n)
    return answer
    
print(solution("P", 15))
print(solution("a     b", 1))
print(solution("a b ", 1))

