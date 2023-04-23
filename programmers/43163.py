'''
[시도1]
1. 단어 간 관계를 파악해서 그래프 만들기
    1.1 한글자만 달라야 간선 생성 - 함수화..
    1.2 
2. target이 가장 먼저 나오는 층 찾기 -> bfs
[시도2]
2. queue 출력해보니 생각했던 순서가 아니라서 dfs로 변경해봄
	2.1. 리프노드가 target이어야 끝나기 때문에 dfs로 리프까지의 경로 확인
	2.2. 오른쪽부터 탐색을 했다 = 나중에 추가된 노드부터 확인
'''
from collections import defaultdict

def dfs(graph, start, end):
    visited, stack = [], []
    stack.append(start)

    while stack:
        node = stack.pop()
        if node not in visited:
            if node == end:
                return len(visited)
            visited.append(node)
            stack.extend(graph[node])

    return len(visited)

def isSimilar(before, after):
    cnt = 0
    for b, a in zip(list(before), list(after)):
        if b != a:
            cnt += 1
    if cnt == 1:
        return True
    return False    
    
def solution(begin, target, words):
    if target not in words:
        return 0
    
    n = len(begin)
    words = [begin] + words
    graph = {w: [] for w in words}

    for idx, w in enumerate(words):
        for s in words[:idx]:
            if isSimilar(s, w):
                graph[s] += [w]
    # print(graph)
    return dfs(graph, begin, target)