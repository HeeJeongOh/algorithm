'''
[시도1] 7.7
1. computers : 인접 행렬 그래프
2. dfs
    2.1 0을 시작으로 탐색
    2.2 마지막 연결노드로 탐색이 끝나면 연결이 되지 않은 새로운 노드 추가
    2.3 반복
    
[시도2]
(원인) if i > node : 
    뒷 번호를 먼저 visited에 삽입되면 위 조건으로 앞 번호와 뒷 번호의 연결성 파악 불가
    (반례) (4, [[1, 1, 0, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 1]]), 1)
'''
def solution(n, computers):
    cnt = 0

    stack = [0]
    visited = []

    while True:
        if len(stack) == 0:
            cnt += 1            
            tmp = [i for i in range(n) if i not in visited]
            if tmp:
                stack.append(tmp.pop())
            else:
                break
            
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            for i, c in enumerate(computers[node]):
                if c == 1:
                    stack.append(i)
            
    return cnt