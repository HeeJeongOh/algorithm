x = 34253
y = 12

def solution(x):
    answer = False
    str_x = str(x)
    q = 0
    for i in range(len(str_x)):
        q += int(str_x[i])
    
    if x % q == 0:
        answer = True
        
    return answer

print(solution(x))
print(solution(y))