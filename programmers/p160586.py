'''
1. target 문자가 keymap에 존재하지 않을 경우, -1
2. 존재할 경우, 해당 문자가 i번째라면 cnt += (i+1)
3. 최소 횟수여야하므로, keymap[n] 중 작은 값 찾아야 함.
4. alphabet dictionary를 만들까 .
    4.1 keymap에 존재하는 문자들로 dict 생성
    4.2 생성 시, 더 작은 값으로 업데이트
'''
from collections import defaultdict
def solution(keymap, targets):
    answer = []
    d = defaultdict(int)
    for key in keymap:
        for i, k in enumerate(key):
            if k in d and i+1 > d[k]:
                continue
            d[k] = i+1
    
    for target in targets:
        cnt = 0
        for t in target:
            if t not in d:
                cnt = -1
                break
            cnt += d[t]
        answer.append(cnt)
        
    return answer