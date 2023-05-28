'''
1. idx = N 사용횟수, dp[idx] = [나올 수 있는 값들]
    1.1 dp[2]까지는 예상 가능하나 dp[3] 규칙을 모르겠음
    1.2 dp[1] = [N]
        dp[2] = [N+N, N-N, N//N, N*N, N*10+N]
2. 풀이 검색
    2.1 NN* 인 num 예외처리
    2.2 
'''

def solution(N, number):
    dp = [[0 for _ in range(8)] for _ in range(8)]
    for i in range(8):
        dp[i].append(int(str(N)*(i+1)))
        for j in range(i):
            for arg1 in dp[j]:
                for arg2 in dp[i-j-1]:
                    dp[i].append(arg1 + arg2)
                    dp[i].append(arg1 - arg2)
                    dp[i].append(arg1 * arg2)
                    if arg2 != 0:
                        dp[i].append(arg1 // arg2)

        if number in dp[i]:
            return i+1
    return -1