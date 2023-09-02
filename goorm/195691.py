def solution(N, K, board, bombs):	
	final = [[0 for _ in range(N)] for _ in range(N)]
	dy = [1, -1, 0,  0, 0]
	dx = [0, 0, 0, 1, -1]
	
	for [i, j] in bombs:
		i = int(i) - 1
		j = int(j) - 1
		for k in range(5):
			y = i + dy[k]
			x = j + dx[k]

			if 0 <= y < N and 0 <= x < N:
				if board[y][x] == '@':
					final[y][x] += 2
				elif board[y][x] == "#":
					final[y][x] += 0
				else:
					final[y][x] += 1
					
	return max(sum(final, []))	

														 
N, K = map(int, input().split())
board = [input().split() for _ in range(N)]
bombs = [map(int, input().split()) for _ in range(K)]
print(solution(N, K, board, bombs))