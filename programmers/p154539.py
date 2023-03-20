'''
1. std를 기준으로 std 뒤에 있는 숫자들 모두 확인 -- 82.6 (시간초과)
2. 예외처리를 위해 if문 삽입 시, 오히려 더 이른 시간초과 발생
3. 힌트: stack 활용 ?
'''
def solution(numbers):
    answer = []
    nlen = len(numbers)
    for i in range(nlen):
        std = numbers[i]
        for j in range(i, nlen):
            if std < numbers[j]:
                answer.append(numbers[j])
                break
            elif j == (nlen-1):
                answer.append(-1)
        
    return answer