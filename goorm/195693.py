'''
[시도1] 
 20/26 : for문 범위 잘못 설정
[시도2] 
 통과
'''
def solution(N, a, b):	
	large = max(a, b)
	small = min(a, b)
	
	for i in range(N // large+1):
		tmp, answer = N, 0
		
		answer += (tmp // large - i)
		tmp -= (large * (tmp // large - i))
		
		answer += tmp // small
		tmp -= small * (tmp // small)

		if tmp == 0:
			return answer
	return -1

N = int(input())
a, b = map(int, input().split())
print(solution(N, a, b))