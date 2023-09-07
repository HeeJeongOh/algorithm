'''
[최종]
 - visited에 값을 저장하는 방식이 시간초과의 원인
'''
def solution(N, town):
	answer = 0
	dy = [1, -1, 0, 0]
	dx = [0, 0, 1, -1]
	for i in range(N):
		for j in range(N):
			# print([i, j])
			if town[i][j] == 1:
				# print("v", visited)	
				answer += 1
				town[i][j] = -1
				q = [[i, j]]
				while q:
					y1, x1 = q.pop(0)
					for k in range(4):
						y2 = y1 + dy[k]
						x2 = x1 + dx[k]
						if 0 <= y2 < N and 0 <= x2 < N and town[y2][x2]== 1:
							town[y2][x2] = -1
							q += [[y2, x2]]
	
	return answer

N = int(input())
town = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, town))

def solution(N, town):
	answer = 0
	dy = [1, -1, 0, 0]
	dx = [0, 0, 1, -1]
	for i in range(N):
		for j in range(N):
			# print([i, j])
			if town[i][j] == 1:
				# print("v", visited)	
				answer += 1
				town[i][j] = -1
				q = [[i, j]]
				while q:
					y1, x1 = q.pop(0)
					for k in range(4):
						y2 = y1 + dy[k]
						x2 = x1 + dx[k]
						if 0 <= y2 < N and 0 <= x2 < N and town[y2][x2]== 1:
							town[y2][x2] = -1
							q += [[y2, x2]]
	
	return answer

N = int(input())
town = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, town))

'''
[시도1] 
 - 감이 잡히지 않아 qna 확인 - 그래프 키워드 확인
 - dfs/bfs로 연결되는 그래프의 개수 = 발전기 개수
[시도2]
 - visited를 계속 갱신하는 상황 수정 visited += []
 - 포문을 이용해서 모든 지점을 확인하는 상황 제거 
 
def solution(N, town):
	answer = 0
	dy = [1, -1, 0, 0]
	dx = [0, 0, 1, -1]
	visited =[]
	
	i, j = 0, 0
	while i < N and j < N:
			# [i, j] 시작노드를 기준으로 연결된 노드 모두 찾기
		if town[i][j] == 1 and [i, j] not in visited:
			# print('\nstart', [i, j])	
			answer += 1
			visited += [[i, j]]
			queue = [[i, j]]
			while queue:
				y1, x1 = queue.pop()
				for k in range(4):
					y2 = y1+ dy[k]
					x2 = x1+ dx[k]
					if 0 <= y2 < N and 0 <= x2 < N and [y2, x2] not in visited and town[y2][x2] == 1:
						visited += [[y2, x2]]
						queue += [[y2, x2]]
						# print(y2, x2)
						i, j = y2, x2
			# print(visited)
		# 다음 칸 확인하기
		if j == N-1:
			i += 1
			j = 0
		else:
			j += 1
			# print('v', visited)
	return answer

N = int(input())
town = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, town))
'''