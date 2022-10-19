# 최장부분수열(LIS) : 일부 수를 제거하여 가장 긴 오름차순 부분수열 만들기
# https://namu.wiki/w/최장%20증가%20부분%20수열
# https://seohyun0120.tistory.com/m/entry/가장-긴-증가하는-부분-수열LIS-완전-정복-백준-파이썬


import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().split()))

dp = [1 for _ in range(N)]

# 자기 자신 이전의 값들 모두 확인해가며 갱신
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+1)

max_dp = max(dp)
print(max_dp)

# 반대 방향으로 가는 이유
# ㄴ 다시 작은 수가 나왔을 때 세는 것이 더 많은 경우의 수가 생김 
max_idx = dp.index(max_dp)
lis = []

while max_idx >= 0:
    if dp[max_idx] == max_dp:
        lis.append(str(A[max_idx]))
        max_dp -= 1
    max_idx -= 1

lis = ' '.join(lis[::-1])
print(lis)