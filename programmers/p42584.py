'''
[시도1] 완전탐색 - 실패 9 시간초과 5 / 15

def solution(prices):
    answer = []
    for i, p in enumerate(prices[:-1]):
        if p > prices[i+1]:
            answer += [1]
        else:
            cnt = 0
            for np in prices[i+1:]:
                if p <= np:
                    cnt += 1
            answer += [cnt]
    answer += [0]
    return answer
'''

'''
[다른사람풀이]
(sol1)
 - 이중포문 - O(n2)
 - else문을 삽입하여 불필요한 연산과정 제거
 - 마지막 값은 항상 0 이기에 제외하고 계산
'''
def solution(prices):
    answer = []
    for i in range(len(prices) - 1):
        sec = 0
        for j in range(i, len(prices) - 1):
            if(prices[i] <= prices[j]):
                sec += 1
            else:
                break
        answer.append(sec)
    answer.append(0)
    return answer
'''
(sol2)
 - 스택 이용 - O(n)
 - 스택에서 꺼내면서 샀던 기간과 현재 기간 빼기
 - 스택을 전부 쳐내면서 얼마의 기간동안 이득봤는지 계산
'''
def solution(prices):
    answer = [0] * len(prices)
    stack = [[prices[-1], 0]]

    for i in range(len(prices) - 2, -1, -1):
        price = prices[i]
        # print(price, stack)
              
        # popCount(얼마의 기간 동안 이득인가)를 세기 위한 부분
        popCount = 1
        while stack and price <= stack[-1][0]:
            _ , count = stack.pop()
            popCount += count
            
        stack.append([price, popCount])
        answer[i] = popCount

    return answer