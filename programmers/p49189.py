'''
[시도1]
ㄴ 이렇게 하니까 3번 노드를 2번 타고 지나 간것으로 취급
1. 가장 멀리 떨어진 노드 -> 리프노드 -> dfs
    1.1 while + stack + visited + pop()
2. 탐색하면서 기록남기기
    2.1 그래프를 한 번 돌 때 1로부터 거리 아는 방법 - 검색
        => stack에 추가할 때 거리 넣기
[시도2]
1. bfs로 탐색해야 함
'''
def solution(n, edge):
    answer = []
    # 그래프 생성
    g = {i: [] for i in range(1, n+1)}
    for a, b in edge:
        g[a] += [b]
        g[b] += [a]
    
    # BFS
    visited = set()  # 방문한 노드를 저장하는 집합
    stack = [(1, 0)]  # 스택에 (노드, 거리) 튜플로 저장
    while stack:
        v, d = stack.pop(0)
        if v not in visited:
            visited.add(v)
            answer.append(d)
            # 인접한 미방문 노드를 스택에 추가하고 거리를 업데이트
            stack.extend((t, d + 1) for t in g[v] if t not in visited)

    return answer.count(max(answer))