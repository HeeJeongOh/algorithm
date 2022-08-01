'''
# 시간초과 : 정확성: 50.0 + 효율성: 0.0
def solution(participant, completion):
    for c in completion:
        participant.remove(c)
    return participant[0]
'''
def solution(participant, completion):
    c = sorted(completion)
    p = sorted(participant)
    # 0, 1
    for i in range(len(c)):
        if c[i] != p[i]:
            return p[i]
    return p[-1]