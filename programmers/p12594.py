x = 2
n = 5

def solution(x, n):
    answer = []
    for i in range(n):
        answer += [x*(i+1)]
    return answer

print(solution(x,n))