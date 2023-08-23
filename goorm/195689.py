'''
1. 완전탐색하면서 깃발 갱신
2. 깃발에 의한 1과 기존 구름 1 구별하기 위해 9로 변형
'''

def solution(N, K, maps):
	answer = 0
	for i in range(N):
		for j in range(N):
			tmp = 0
			if maps[i][j] == 0:
			# 상하좌우 + 대각선 확인하기ㄱㅣ
				for dy in range(-1,2):
					for dx in range(-1, 2):
						if dy == 0 and dx == 0:
							continue
						if 0 <= i+dy < N and 0 <= j+dx < N and maps[i+dy][j+dx] >= 9: 
							tmp += 1
				if tmp > 0:
					maps[i][j] = tmp

			if tmp == K:
				answer += 1
	# for i in range(N):
		# print(maps[i])
	return answer
	

N, K = map(int, input().split())
maps = [[9 if m == '1' else int(m) for m in list(input().split())] for _ in range(N)]
print(solution(N, K, maps))