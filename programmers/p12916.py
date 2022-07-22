# 단순 비교
def solution(s):
    p_cnt = 0
    y_cnt = 0
    for i in range(len(s)):
        if s[i] == 'p' or s[i] == 'P':
            p_cnt += 1
        elif s[i] == 'y' or s[i] == 'Y':
            y_cnt += 1
    if p_cnt == y_cnt:
        return True
    else:
        return False
        
# 라이브러리 활용
def solution(s):

    s = s.lower()
    substring1 = "p"
    substring2 = "y"

    x = s.count(substring1)
    y = s.count(substring2)

    return (x == y)