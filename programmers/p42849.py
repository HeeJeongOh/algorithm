''' 이전 통과
def solution(answers):
    answer = [] # 가장 많이 맞은 사람
    counts = [] # 맞은 개수
    
    # 수포자 정보
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    people = [p1, p2, p3]
    
    # 시험문제 수
    size = len(answers)    
    # 수포자 각각에 대해 맞은 개수 세기
    for p in people:
        cnt = 0
        for i in range(size):
            if p[i % len(p)] == answers[i]:
                cnt = cnt + 1        
        counts.append(cnt)
    
    max = counts[0]
    answer.append(1)    
    for i in range(1,3):
        if counts[i] > max:
            answer.pop()
            max = counts[i]
            answer.append(i+1)
            
        elif counts[i] == max:
            answer.append(i+1)
    
    return answer
'''

# 런타임에러
def solution(answers):
    answer = []
    l = len(answers)
    # 각각의 수포자 주기
    s = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    # 채점표            
    result = [0,0,0]
    # 수포자의 답안지
    for i in range(3):    
        for j in range(l):
            if answers[j] == s[i][j % l]:
                 result[i] += 1
    
    m = max(result)
    for i in range(3):
        if m == result[i]:
            answer.append(i+1)

    return answer