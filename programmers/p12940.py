def solution(n, m):
    answer = []
    # 최대공약수
    for i in range(m, 0, -1):
        if n % i == 0 and m % i == 0:
            answer.append(i)
            break
    # 최소공배수
    a = n // answer[0]
    b = m // answer[0]
    answer.append(a*b*answer[0])
    
    return answer