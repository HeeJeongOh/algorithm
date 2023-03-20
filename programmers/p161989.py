'''
1. m칸 짜리 막대기를 이동해간다고 생각함 -- 80.0
2. 시작점 업데이트를 놓침 ; for문 내
    idx +=  m -> idx = sec + m
'''
def solution(n, m, section):
    cnt = 1
    # 다음 색칠을 시작할 칸의 인덱스
    idx = section[0] + m
    for sec in section[1:]:
        if sec >= idx:
            cnt += 1
            # 색칠 시작점 업데이트
            idx = sec + m
    return cnt