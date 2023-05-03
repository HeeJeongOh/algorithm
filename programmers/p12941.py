'''
1. 두 수의 곱의 누적합이 최소가 되도록
2. 가장 큰 수랑 가장 작은 수 곱하기
'''
def solution(A,B):
    answer = 0
    size = len(A)
    
    A.sort()
    B.sort(reverse=True)
    
    for a, b in zip(A, B):
        answer += (a*b)
    
    return answer