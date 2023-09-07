'''
[시도1] 8/26
1. K로 누릴 수 있는 최대의 포만감 합
2. c/p를 기준으로 정렬하고 하나씩 빼가기 마지막만 신경쓰기
[시도2]
1. 마지막의 경우 
2. 돈을 모두 쓰지 않을 수도 있음
'''
def solution(N, K, pc):
	cfinal = 0
	pc.sort(key=lambda x : (x[1]/x[0], x[0]), reverse=True)
	# print(pc)
	for i, (p, c) in enumerate(pc):
		if K-p >= 0:
			K -= p
			cfinal += c
		else:
			cfinal += (pc[i][1]/pc[i][0])*K
			break
		
		# print([p, c], K, cfinal)
	return int(cfinal)

N, K = map(int, input().split())
pc = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, K, pc))