'''
1. 종류가 제한적 -> 글자수 2 또는 3으로 경우 나누기
2. 발음할 수 잇는 경우만 answer += 1 
3. 연속해서 같은 발음인 경우 제외하기
    3.1 이전 단어 저장
'''
def solution(babbling):    
    answer = 0
    for b in babbling:
        i, tmp = 0, 0
        flag = True
        preword = ''
        while i < len(b):          
            if preword == b[i:i+2] or preword == b[i:i+3]:
                flag = False
                break
            
            if (b[i] == 'a' or b[i] == 'w') and b[i:i+3] in ['aya', 'woo']:
                preword = b[i:i+3] 
                i += 3
            elif (b[i] == 'y' or b[i] == 'm') and b[i:i+2] in ['ye', 'ma']:
                preword = b[i:i+2]
                i += 2                
            else:
                flag = False
                break
                  
        if flag:
            # print(b)
            answer += 1
                    
    return answer