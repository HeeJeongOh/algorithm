'''
S, D, T = 1제곱, 2제곱, 3제곱 
* = 해당 점수와 바로 전에 얻은 점수를 각 2배로
# = 해당 점수는 마이너스

1. 93.8 ->  실패 tc18, 22
    ㄴ '질문하기' 확인, tc 추가
2. 100.0 
    ㄴ 값 저장과 연산을 분리하여 작성했으나 생각해보니 한 번에 가능하여 수정
'''

def solution(dartResult):   
    answer = 0
    dict = {'S': 1, 'D': 2, 'T': 3}

    tmp = []
    # 점수 | 보너스 | [옵션]
    for i in range(len(dartResult)):
        if dartResult[i].isalpha():
            continue
        if dartResult[i].isdigit():            
            if dartResult[i:i+2] == '10':
                score = 10
                bonus = dict[dartResult[i+2]]
                i += 1
            else:
                score = int(dartResult[i])
                bonus = dict[dartResult[i+1]]   
            tmp.append(score**bonus)
        elif dartResult[i] == '*':
            if len(tmp) < 2:
                tmp.append(tmp.pop()*2)
            else:
                a = tmp.pop()
                b = tmp.pop()
                tmp.append(b*2)
                tmp.append(a*2)
        elif dartResult[i] == '#':
            tmp.append(-tmp.pop())
    
    answer = sum(tmp)

    return answer
    
# 72
dR = '1S2D*3T*'
print(solution(dR))

'''
def solution(dartResult):   
    answer = 0
    dict = {'S': 1, 'D': 2, 'T': 3}
    flag = False

    splits = []
    # 점수 | 보너스 | [옵션]
    for i in range(len(dartResult)):
        if dartResult[i].isalpha():
            continue
        if dartResult[i].isdigit():            
            if dartResult[i:i+2] == '10':
                score = 10
                bonus = dict[dartResult[i+2]]
                i += 1
            else:
                score = int(dartResult[i])
                bonus = dict[dartResult[i+1]]   
            splits.append(score**bonus)
        else:
            splits.append(dartResult[i])
    
    tmp = []
    for s in splits:
        if s == '*':
            if len(tmp) < 2:
                tmp.append(tmp.pop()*2)
            else:
                a = tmp.pop()
                b = tmp.pop()
                tmp.append(b*2)
                tmp.append(a*2)
        elif s == '#':
            tmp.append(-tmp.pop())
        else:
            tmp.append(s)
        print(tmp)

    answer = sum(tmp)

    return answer
'''