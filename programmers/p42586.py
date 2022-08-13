# 문제 분류를 확인하고 나서야 문제풀이 방향성 잡음 :(
import math

def solution(progresses, speeds):
    answer = []
    needs = []
    for p, s in zip(progresses, speeds):
        needs.append(math.ceil((100-p)/s))

    stack = []
    std = needs[0]
    for i in range(len(needs)):
        if needs[i] <= std:
            stack.append(needs[i])
        else:
            answer.append(len(stack))
            stack.clear()

            stack.append(needs[i])            
            std = needs[i]
        
    answer.append(len(stack))
    return answer

p = [93, 30, 55]	
s = [1, 30, 5]	
r = [2, 1]
print(solution(p, s) == r)