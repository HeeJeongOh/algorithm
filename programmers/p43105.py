def solution(triangle):
    triangle = [[0] + t + [0] for t in triangle]
    print(triangle)

    for i in range(1, len(triangle)):
        for j in range(1,i+2):
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

    return max(triangle[-1])


t = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(t))

# 23-04-03
'''
0. 전에 풀었던 문제인데 풀이 이해 위주로 정리
1. 문제의 생김새를 통해 DP 유형 추측 가능
2. 한 층씩 내려가면서 값을 갱신해나감
'''
def solution(triangle):
    answer = 0
    # 인덱스 에러 피하기 위함.
    triangle = [[0] + t + [0] for t in triangle]
    # 1행 씩 내려가는 포문
    for i in range(1, len(triangle)):
        # 각각에 대해 선택할 수 있는 이전 값 중 최댓값을 더해 저장
        for j in range(1,i+2):
            # 더해나갈 수 있는 범위가 (i-1, j-1), (i-1, j) 만 존재.
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    # 마지막 리프의 경로합 중 최대 선택
    return max(triangle[-1])