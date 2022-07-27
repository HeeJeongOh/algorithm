def solution(arr, divisor):
    answer = []
    for a in arr:
        if a % divisor == 0:
            answer.append(a)
            answer.sort()
    '''
    if len(answer) == 0:
        answer.append(-1)
        
    return answer
    ''' 
    # or 앞이 참일경우 해당 값까지만 , 거짓일 경우 뒤에 것까지 호출
    return sorted(arr) or [-1]