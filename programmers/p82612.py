'''
# 이전 풀이
def solution(price, money, count):
    answer = -1
    use = 0
    
    for i in range(1, count+1):
        use += (price*i)
    
    if money < use:
        answer = use - money
    else:
        answer = 0
        
    return answer
'''

def solution(price, money, count):
    need = 0
    for i in range(1, count+1):
        need += price*i
    if need-money <= 0:
        return 0
    else:
        return need-money
