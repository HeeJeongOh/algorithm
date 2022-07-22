# string.isalpha() : 모두 알파벳인 경우 True 반환
# string.isnumeric() : 모두 숫자인 경우 True  반환
def solution(s):
    if len(s) != 4 and len(s) != 6:
        return False
    for i in range(len(s)):
        if s[i].isalpha():
            return False        
    return True

def solution2(s):
    if len(s) != 4 and len(s) != 6:
        return False
    if s.isnumeric():
        return True
    else:
        return False

print(solution('a234'))
print(solution2('1234'))