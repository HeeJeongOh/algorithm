'''
[시도1] 시간초과 6/20
1. arr = [] : 1행 1열부터 i행 i열까지의 영역 내의 모든 빈 칸을 숫자 i로 채우기
    0-(i-1) : [i+1]
    i-n     : [j+1]
2. result = 각 행을 연결하여 1차원 배열로 만들기
3. return result[left:right+1]

[시도2] 시간초과 7/20
1. 애초에 1차원 배열로 만들기
2. 동일

[시도3]
1. 전체에서 [left, right] 추출이 아닌 필요한 부분만 구하기
'''
def solution(n, left, right):
    result = []
    for idx in range(left, right+1):
        # row행, col열
        row = idx // n 
        col = idx % n
        
        if col < row:
            result.append(row+1)
        else:
            result.append(col+1)
    
    return result