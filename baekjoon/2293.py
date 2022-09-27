import sys

n, k = map(int, sys.stdin.readline().split())
coins = []
for _ in range(n):
    c = int(sys.stdin.readline().rstrip())
    coins.append(c)

# output : coins를 활용하여 k를 만들 수 있는 경우의 수 (단, 순서가 달라도 같은 것으로 봄)
# 중복조합 : 5a + 2b + 1c = k => 구현 X
# 구글링
dp = [0 for _ in range(10001)]
dp[0] = 1
for i in range(n):
    for j in range(coins[i], k+1):
        dp[j] += dp[j-coins[i]] 

print(dp[k])