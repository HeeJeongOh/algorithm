'''
1.과거를 기억해야하면 스택 사용하기
    1.1. 마지막 괄호가 ( 이면 바로 false 
    1.2. ( 이면 push
    1.3. ) 이면 이전 스택에 있는 것과 비교하여 닫히면 pop
    
[시도1] 
    정확성: 50.2 - 런타임에러4 : 빈 스택인 경우 에외 처리, 실패1
    효율성: 15.2
[시도2]
    정확성: 65.7 - 실패1 : 스택이 모두 비어있지 않은 경우에도 false 반환
    효율성: 15.2 - 실패1
'''
def solution(s):
    if s[-1] == '(':
        return False
    stack = []
    for tmp in s:
        if tmp == '(':
            stack.append(tmp)
        else:
            # (+) try-catch와 IndexError 활용 가능.
            if len(stack) == 0:
                return False
            if stack[-1] == '(':
                stack.pop()
                
    # (+) return len(stack) == 0 으로 수정 가능.
    if len(stack) != 0:
        return False
    
    return True


