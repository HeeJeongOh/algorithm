def solution(w, r):
	ans = w * (1 + r / 30)
	return int(ans)
	
w, r = input().split()
print(solution(int(w),int(r)))
