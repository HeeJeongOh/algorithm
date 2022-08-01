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