'''
1. 런타임에러 - 주로 배열 인덱스 실수
    ㄴs[i][j % l] --> s[i][j % len(s[i])]
    ㄴ 수포자의 주기가 답안보다 짧을 경우에 대한 예외처리 잘못 작성
'''
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
            if answers[j] == s[i][j % len(s[i])]:
                 result[i] += 1
    
    m = max(result)
    for i in range(3):
        if m == result[i]:
            answer.append(i+1)

    return answer

'''
1. 이전에 풀었던 문제 - 수포자 규칙성 상수로 저장
   ㄴ 규칙성이 없기 때문에 동일하게 푸는 게 베스트일 듯
2. 이전보다 깔끔하게 정리해봄.
'''

def solution(answers):
    student = [[],
               [1, 2, 3, 4, 5],
               [2, 1, 2, 3, 2, 4, 2, 5],
               [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    scores = [-1, 0, 0, 0]
    
    for i, a in enumerate(answers):
        if student[1][i % len(student[1])] == a:
            scores[1] += 1
        if student[2][i% len(student[2])] == a:
            scores[2] += 1
        if student[3][i % len(student[3])] == a:
            scores[3] += 1
    
    nmax = max(scores)
    answer = [i for i, s in enumerate(scores) if s == nmax]
    
    return answer