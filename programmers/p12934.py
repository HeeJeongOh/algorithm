def solution(n):
    answer = -1
    x = n**(1/2)
    if x == int(x):
        return (x+1)**2
    return answer

print(solution(121))
print(solution(123))