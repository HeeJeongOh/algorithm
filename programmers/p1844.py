'''
상대 팀 진영에 더 빨리 도착하기 - (n-1, m-1)칸에 가는 최소방법

[시도1] : 12.8 + 0.0 = 12.8 / 100.0
1. 상대팀 진영이 벽에 둘러싸인 경우, return -1
2. 상대팀 진영 접근 최소방법 = 합이 적은 것.
    2.1 dfs로 리프까지의 합을 더해나가서 최소 반환하기 ?
    2.2 bfs 최단거리
3. 그래프 만들기
    3.1 길 찾기 (a-1, b), (a+1,b), (a, b+1), (a, b-1)
    
[시도2] 25.6 + 22.6 = 48.1 / 100.0 (실패 + 런타임에러)
ㄴ 힌트: https://school.programmers.co.kr/questions/46776
1. 상하좌우로 움직이는 방법에 대한 새로운 방법
2. maps[x][y] == 1 : 방문하지 않았으면서 길이 존재하는 곳
    -> visited 필요 없음
    
[시도3]
1. 참고한 답안과 m, n 선언이 뒤바뀜
'''        
def solution(maps):
    answer = -1
    m = len(maps)
    n = len(maps[0])
    
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    stack = [(0, 0)]
    
    while len(stack) > 0:
        x, y = stack.pop(0)
                
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 1이 아닌 경우, 이미 방문하거나 길이 막힌 것이므로 visited 필요없음
            if 0 <= nx < m and 0 <= ny < n and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                stack.append((nx,ny))

    return maps[m-1][n-1] if maps[m-1][n-1] != 1 else -1