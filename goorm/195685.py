def solution(T, problems):
	ans = 0
	for p in problems:
		a, op, b = p.split(" ")
		a, b= int(a), int(b)
		if op == '+':
			ans += (a + b)
		elif op == '-':
			ans += (a - b)
		elif op == '*':
			ans += (a * b)
		elif op == '/':
			ans += (a // b)
	return ans

# 입력 받기
T = int(input())
problems = [input() for _ in range(T)]
print(solution(T, problems))
