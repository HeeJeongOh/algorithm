'''
0. k : 최상품 사과 / 한 상자는 m개의 사과로 이루어짐 / 한 상자의 가격 = p*m
1. 이익 = sum ((최저 사과 점수) x (한 상자에 담긴 사과 개수))
2. box = 내림차순 slicing 하여 넣기
'''
def solution(k, m, score):
    score.sort(reverse = True)
    box = []
    for i in range(0, len(score), m):
        # slicing 하면 나머지 모두 추가 -> 3개만 있으도 3개 추가
        tmp = score[i:i+m]
        if len(tmp) == m: 
            box.append(tmp)
    return sum(min(b)*m for b in box)
