def solution(N, T, M):
	# 24시간마다 60분마다 초기화 - 나머지 연산 
	for i in range(N):
		tmp = M + int(input())
		T = (T + (tmp) // 60) % 24
		M = (tmp % 60)

	return str(T) + " " + str(M)
			
# 입력
N = int(input())
T, M = map(int, input().split())
print (solution(N, T, M))
