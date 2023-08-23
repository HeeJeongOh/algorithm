'''
0. 통증수치를 0으로 줄이기 위한 최소한의 아이템 개수
1. 큰 숫자부터 최대한 활용하기
'''
def solution(N):
	answer = 0
	meds = [14, 7, 1]
	
	for i in range(3):
		answer += N // meds[i]
		N = N % meds[i]
	return answer

N = int(input())
print(solution(N))