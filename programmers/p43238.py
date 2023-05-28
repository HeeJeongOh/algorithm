'''
0. 이분탐색 개념 학습 -> 어떻게 적용해할지 모르겠음
[시도1] : 0.0 (3실패, 7시간초과) / 100.0
1. 최대한 실제상황과 비슷하게 설계
2. times와 동일한 리스트 생성
    2.1 process = times -> call by ref.(직접참조)
    2.2 process = times.copy() -> call by value.(값)
3. 시간이 지남에 따라 process 모두 마이너스
    3.1 0이되면 n--, 다시 기본값 넣기
def solution(n, times):
    cnt = 0
    process = times.copy()
    size = len(times)
    n -= size
    while n > 0:
        for i in range(size):
            if process[i] == 1:
                process[i] = times[i]
                n -= 1
            process[i] -= 1
        cnt += 1
    
    return cnt + max(process)
[시도2]
ㄴ 입출력 설명 중 20분이 되었을 때 2번째가 아닌 1번째로 선택함
1. 소요시간의 경우의 수가 정해져있음
    1.1 
2. 이분 탐색을 통해 해당 경우로 처리가 가능한지 확인
    2.1 target : sum(m//i for i in times)
        ㄴ 각 심사관에게 최대 사람 수를 부여했을 때 합
'''
def solution(n, times):
    # 소요시간 최소값, 최댓값
    start = 0
    end = n*times[-1]

    while start < end:
        # 소요시간의 중앙값
        m = (start + end) // 2
        # m // times[i] : 각 심사관이 차지할 사람 수
        # n <= sum(m//i for i in times) : 더 적은 소요시간으로 심사대상 모두 심사 가능
        # ㄴ 심사대상 <= 모든 심사관이 차지할 수 있는 사람 수
        if n <= sum(m // i for i in times):
            end = m
        else:
            start = m+1
    return start


