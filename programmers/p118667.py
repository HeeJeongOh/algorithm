'''
0. 큐는 먼저 집어넣은 원소가 먼저 나오는 구조
1. 시간초과 (60/100) 
    => for문 횟수 증가, 홀수 합 조기종료 세팅,  (질문하기) sum함수 사용 X
2. 시간초과 (93.3/100) 
    => for문 대신 while문을 통해 q1, q2 위치가 모두 바뀌는 종료조건 추가
3. (참고) 합을 계속 계산하지 말고 target과 값을 비교해가며 풀이 가능
'''
from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)

    sum_q1 = sum(q1)
    sum_q2 = sum(q2)
    cnt = 0
        
    # 애초에 합이 짝수가 아닌 경우, 합이 같아질 수 없음
    if (sum_q1 + sum_q2) % 2 != 0:
        return -1

    # 최대횟수 고려 : q1과 q2가 모두 뒤바꼈을 때
    # for문 횟수 넉넉하게 변경
    i, j = 0, 0
    qlength = len(q1)+1
    while i<2*qlength and j<2*qlength:
        print(q1, q2)        
        if sum_q1 == sum_q2:
            return cnt
            
        if sum_q1 > sum_q2:
            i += 1
            n = q1.popleft()
            q2.append(n)
            sum_q1 -= n
            sum_q2 += n
        elif sum_q1 < sum_q2:
            j += 1
            n = q2.popleft()
            q1.append(n)
            sum_q2 -= n
            sum_q1 += n
            
        cnt += 1
        
    return -1

q1 = [1, 2, 1, 2]
q2 = [1, 10, 1, 2]
print(solution(q1, q2))
# q1 = [1,1,1,8,10,9] 
# q2 = [1,1,1,1,1,1] 
# print(solution(q1, q2))
