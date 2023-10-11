'''
[시도1] 실패 1 시간초과 3 / 8
0. 모든 섬이 서로 통행 가능하도록 만들 때 필요한 최소 비용 return
1. (n-1)개의 선을 선택해야한다고 생각 -> 조합
    1.1 주어진 costs 중 (n-1)개 선택
    1.2 모든 섬을 지나는 경우에 cost 저장해두기

from itertools import combinations
def solution(n, costs):
    if n == 1:
        return 0
    elif n == 2:
        return costs[0][2]
    
    answer = 10000000000
    for nums in list(combinations(range(len(costs)), n-1)):
        land = set()
        cost = 0
        for tmp in nums:
            a, b, c = costs[tmp]
            land.update([a, b])
            cost += c

        if list(land) == list(range(n)) and answer > cost:
            answer = cost
    # print(answer)
    return answer

[시도2] 질문하기 힌트 참고
1. cost를 기준으로 정렬하기 : 최소 cost를 갖고자하니까
2. 기준 아이템을 선택한 상태로 모두 순회할 수 있는 나머지 고르기
	ㄴ 
=> 테케는 모두 통과하나 제출하면 런타임에러1 실패6 / 8

def solution(n, costs):
    if n == 1:
        return 0
    elif n == 2:
        return costs[0][2]
    
    answer = [1000000]
    costs.sort(key=lambda x: (x[2]))
    print(costs)
    for i, (frm, to, cost) in enumerate(costs):
        land = set([frm, to])
        total = cost
        for a, b, c in costs[:i]+costs[i+1:]:
            if a in land or b in land:
                land.update([a, b])
                total += c
            
            if land == {i for i in range(n)}:
                answer += [total]
                break
                
    return min(answer)
'''

'''
https://chanhuiseok.github.io/posts/algo-33/
# 최소신장트리(MST)
- 신장트리 = n 노드 + (n-1) 간선
    - 모든 노드가 적어도 하나의 간선으로 연결
    - 싸이클을 형성하지 않음 
- 크루스칼 알고리즘: 그래프 내의 모든 정점들을 가장 적은 비용으로 연결하기 위함
--
1. 가중치 오름차순으로 정렬
2. 사이클을 형성하지 않는 선에서 순서대로 간선 선택
'''
def solution(n, costs):
    answer = 0
    
    # 각 노드의 부모를 표현한 배열
    # parents[0] = 1 : 0의 부모노드는 1이다.
    parents = [i for i in range(n+1)]
    
    # 어떤 집합에 속해있는지 찾기
    # 재귀적으로 최상위 부모를 찾게 됨.
    def find(n):
        if parents[n] == n:
            return n
        return find(parents[n])
    
    # 서로 다른 두 집합 합치기
    def union(n1, n2):
        # 부모노드 찾기
        p1 = find(n1)
        p2 = find(n2)

        if p1 != p2:
            parents[p1] = p2
            
    # cost를 기준으로 costs 정렬
    costs.sort(key=lambda x: x[2])
    for a, b, c in costs:
        # 두 노드가 같은 부모를 가졌는지 확인
        if find(a) != find(b):
            # 간선을 추가하고 합치기
            union(a, b)
            answer += c

    return answer