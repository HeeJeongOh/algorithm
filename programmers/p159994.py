'''
[시도1] 52.0 / 100.0
ㄴ 문제를 잘못 이해함
1. 순서대로 단어카드를 뽑아 골과 비교
[시도2]
1. cards1과 cards2에 대해 각각의 포인터 생성
2. goal을 기준으로 단어 비교
'''
def solution(cards1, cards2, goal):
    idx1, idx2 = 0, 0
    for g in goal:        
        if idx1 < len(cards1) and g == cards1[idx1]:
            idx1 += 1
        elif idx2 < len(cards2) and g == cards2[idx2]:
            idx2 += 1
        else:
            return 'No'
    return 'Yes'
