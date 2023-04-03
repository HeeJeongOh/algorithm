'''
- 대칭을 이루어야 함.
- food : 음식의 양을 칼로리가 적은 순서로 나타내는 배열
    ㄴ food[i] : i번 음식의 수
    ㄴ food[0] : 물 
'''

def solution(food):
    answer = ''
    for i in range(1, len(food)):
        cnt = food[i]
        if cnt > 1:
            cnt = cnt // 2
            answer += str(i) *cnt           
    answer += ('0' + answer[::-1])

    return answer