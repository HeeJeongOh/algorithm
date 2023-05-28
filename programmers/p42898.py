'''
[시도1] 0.0
1. 최단경로 - bfs -> 게임맵 참고
[시도2] 45.0 + 0.0 = 45.0 / 100.0 <시간초과>
1. puddle : 좌표 (y,x) 
    dp = [[1 for _ in range(m)] for _ in range(n)]
    for p in puddles:
        # 좌표이기 때문에 위치 바꾸기
        x, y = p[1]-1, p[0]-1 
        dp[x][y] = 0

    dxy = [[1,0], [0,1]]
    stack = [(0, 0)]
    while stack:
        x, y = stack.pop()
        for [dx, dy] in dxy:
            nx, ny = x+dx, y+dy
            if nx == n-1 and ny == m-1:
                ans += 1
            if 0 <= nx < n and 0 <= ny < m and dp[nx][ny] == 1:
                stack.append((nx,ny))  
                
[시도3] 
ㄴ (힌트) https://school.programmers.co.kr/questions/27771
1. 

'''
def solution(m, n, puddles):
    ans = 0
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    dp[1][1] = 1
    
    # 행
    for i in range(1, n+1):
        # 열
        for j in range(1, m+1):
            if [j, i] in puddles or [i, j] == [1,1]:
                continue
            else:
                # 
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007

    return dp[n][m]
