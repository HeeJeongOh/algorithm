'''
[시도1]
1. 딕셔너리를 이용해서 각 건물 별 단지 개수 저장
2. 발전기 1과 동일하게 수행
[시도2]
1. 문제를 제대로 보지 않고 '단지의 기준' 적용 x
'''
def solution(N, K, town):
	dy = [1, -1, 0, 0]
	dx = [0, 0, 1, -1]
	mmap = [0 for _ in range(31)]
	
	for i in range(N):
		for j in range(N):
			if town[i][j] > 0:
				t = town[i][j]
				
				town[i][j] = 0
				q = [[i, j]]
				cnt = 1
				while q:
					y1, x1 = q.pop()
					for d in range(4):
						y2 = y1 + dy[d]
						x2 = x1 + dx[d]
						if 0 <= y2 < N and 0 <= x2 < N and town[y2][x2] == t:
							town[y2][x2] = 0
							q += [[y2, x2]]
							cnt += 1
				
				if cnt >= K:
					mmap[t] += 1


	# 최대 단지 수를 가지고 있는 인덱스들 반환
	answer = list(filter(lambda x: mmap[x] == max(mmap), range(len(mmap))))
	# print(answer)
	return max(answer)


N, K = map(int, input().split())
town = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, K, town))