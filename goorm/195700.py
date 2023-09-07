'''
1. 평행인 반직선들을 먼저 찾아볼까
	1.1 두 직선이 평행이라면 겹치는 부분에서 카운트 안 늘리기
	1.2 평행할 수 있는 가로 세로 먼저 구분
2. 가로보드, 세로보드 생성
	2.1 각각 지나가는 점 카운트 
	2.2 zip(가로보드, 세로보드) -> 두 보드의 곱을 더하기
'''
def solution(N, M, hlines):
	dmap = {'U': [-1, 0], 'D': [1, 0], 'L': [0, -1], 'R': [0, 1]}
	# 가로 : board[0] / 세로 : board[1
	board = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(2)]
	
	for h in hlines:
		i = 0 if (h == 'R' or h == 'L') else 1

		for y, x in hlines[h]:
			# print(h, (y, x))
			for _ in range(N):
				if 0 <= y < N and 0 <= x < N:
					board[i][y][x] += 1
					y, x = y + dmap[h][0], x + dmap[h][1]
			# for b in board[i]:
			# 	print(b)
			# print()

	answer = 0
	for b1, b2 in zip(board[0], board[1]):
		# print(b1, b2)
		for i, j in zip(b1, b2):
			# print(i, j)
			answer += (i*j)

	return answer
		
from collections import defaultdict
N, M = map(int, input().split())
hlines = {'U': [], 'D': [], 'L': [], 'R': []}
for _ in range(M):
	tmp = input().split()
	hlines[tmp[2]] += [(int(tmp[0])-1, int(tmp[1])-1)]

print(solution(N, M, hlines))