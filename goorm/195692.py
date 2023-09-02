'''
[시도1] 
 종착지만 저장 -> 지나가는 칸들도 모두 포함해야함.
[시도2]
 하나의 command 내 반복되어도 잡지 못함
[시도3]
 통과
'''
def solution(N, start, cc):	
	answer = [1, 1]
	for i, (y, x) in enumerate(start):
		records = []
		
		while True:
			count = int(cc[y-1][x-1][:-1])
			command = cc[y-1][x-1][-1]
			if (y, x) in records:
				break
				
			# 종착지만 저장 -> 지나가는 칸들도 모두 포함해야함.
			for _ in range(count):
				records.append((y, x))
				if command == 'U':
					y -= 1
					if y <= 0:
						y += N
				elif command == 'D':
					y += 1
					if y > N:
						y -= N
				elif command == 'L':
					x -= 1
					if x <= 0:
						x += N
				elif command == 'R':
					x += 1
					if x > N:
						x -= N
				
				if (y, x) in records:
					break
				else:
					answer[i] += 1

	if answer[0] > answer[1]:
		return "goorm " + str(answer[0])
	else:
		return "player " + str(answer[1])


N = int(input())
start = [map(int, input().split()) for _ in range(2)]
cc = [input().split() for _ in range(N)]
print(solution(N, start, cc))