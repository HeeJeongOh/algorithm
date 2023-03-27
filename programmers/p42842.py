'''
- 갈색 테두리는 1줄, 노란색은 알 수 없음
- 전체 카펫의 가로, 세로 크기
0. 가로 > 세로
1. 노란색 격자의 수를 통해 나올 수 있는 직사각형 조합 찾기
    1.1 넓이 = 격자 수 -> 공약수 활용
    1.2 공약수 구하는 방법 - 나머지 = 0
2. 노란색의 가로, 세로를 통해 전체 둘레(갈색) 파악 가능
    2.1 w = y_w + 2
        h = y_h + 2
    2.2 이때 그 조합들 중 w*h가 갈색 격자의 수와 매칭되는 것을 찾아야 함.
'''
def solution(brown, yellow):
    for i in range(1, int(yellow**(1/2))+1):
        if yellow % i == 0:
            y_w = yellow // i
            y_h = i
            
            w = y_w + 2
            h = y_h + 2

            # sets.append([w, h])
            if w*h == (brown+yellow):
                return [w, h]