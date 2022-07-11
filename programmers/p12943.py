num1 = 16       # 4
num2 = 626331   # -1

def solution(num):
    answer = 0
    while True:
        if num == 1: break
        if answer > 500 :
            return -1
        if num % 2 == 0:
            num = num / 2
        else:
            num = num*3 + 1
        
        answer += 1
        
    return answer

print(solution(num1))
print(solution(num2))