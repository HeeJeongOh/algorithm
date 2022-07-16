def solution(n):
    tmp = str(n)
    l = len(tmp)
    answer = [0 for _ in range(l)]
    for i in range(l):
        answer[l-i-1] = int(tmp[i])
    return answer

def solution2(n):
    answer = list(map(int, reversed(str(n))))
    return answer

print(solution(12345))
print(solution2(12345))