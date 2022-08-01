'''
1. 런타임에러
    ㄴ 나눗셈에서 분모가 0이 되는 예외처리 안함
2. 실패
    ㄴ 예외처리 후, '스테지이 도달 유저가 없을 경우, 실패율 0' 간과
'''
def solution(N, stages):
    answer = []
    clear = [0 for _ in range(N+1)]
    for s in stages:
        for i in range(s-1):
            clear[i] += 1
    clear.pop()  

    p = len(stages)
    tmp = []
    for i in range(len(clear)):
        # 분모가 0이 되는 경우
        if p == 0: break
        tmp.append(((i+1),(p-clear[i]) / p))
        p = clear[i]     
    
    # 스테이지 도달 못한 경우의 실패율
    if len(tmp) < N:
        for i in range(len(tmp), N):
            tmp.append((i+1, 0))
    
    tmp = sorted(tmp, key=lambda x:x[1], reverse=True)
    for t in tmp:
        answer.append(t[0])
        
    return answer