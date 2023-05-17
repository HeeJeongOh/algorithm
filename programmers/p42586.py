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

'''
0. 이전에 푼 문제 - 풀이 확인하지 않고 다시 품 -> :)
[시도1] 90.9 / 100.0
1. 차이 저장 
2. 기준 숫자보다 크면 다음 배포에 포함시키기

[시도2] 
1. 차이 저장 시, int가 아닌 ceil 사용
    ㄴ diff[30] -> 3
'''
import math
def solution(progresses, speeds):
    answer = []
    diff = []
    for p, s in zip(progresses, speeds):
        diff.append(math.ceil((100-p)/s))
        print(diff)

    nstd = diff[0]
    answer.append(0)
    idx = 0
    for d in diff:
        if d > nstd:
            nstd = d
            answer.append(0)
            idx += 1
        answer[idx] += 1
            
    return answer