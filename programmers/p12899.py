# 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력
def solution(n):
    ans = []
    
    while n > 0:
        # q, r
        n, r = divmod(n, 3)
        if r == 0:
            r = 4
            n -= 1
        ans.append(str(r))
    print(ans)
    return "".join(ans[::-1])

n = 3
r = 4
print(solution(n)==r)

n = 10
r = 41
print(solution(n)==r)