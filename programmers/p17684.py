'''
[시도1] 테케 4 통과 X, 50.0 / 100
1. 문제 규칙
    1.1 길이가 1인 모든 단어를 포함하도록 사전을 초기화한다.
    1.2 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다.
    1.3 w에 해당하는 사전의 색인 번호를 출력하고, 입력에서 w를 제거한다.
    1.4 입력에서 처리되지 않은 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록한다.
    1.5 단계 2로 돌아간다.

def solution(msg):
    answer = []
    # 1.1
    dic =  list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    i = 0
    while i < len(msg):
        # 1.2
        for j in range(len(dic[-1]), 0, -1):
            w = msg[i:i+j]
            if w in dic:
                # 1.3
                answer += [dic.index(w)+1]
                i = i+j-1             
                # 1.4
                if i+1 < len(msg):
                    dic += [w+msg[i+1]]
                break
        i += 1
    return answer
'''

'''
[질문하기]
0. dic : 사전 / value : dic에 넣을 인덱스 / base : 현재 입력
1. base가 사전에 있다면
    1.1 answer에 마지막으로 추가한 숫자를 변경
2. 사전에 없다면
    2.1 사전에 추가
    2.2 base를 msg[i]로 변경
'''
def solution(msg):   
		# 0
    dic = {a: i+1 for i, a in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
    
    answer = [0]
    value = 26
    base = ""
    
    for i in range(len(msg)):
        base += msg[i]
        # 1 : K - 6. KA
        if base in dic:
            answer[-1] = dic[base]
        # 2. KA - 4. AK - 7. KAO
        else:
            value += 1
            dic[base] = value

            base = msg[i]
            # 3. A - 5. K - 8. O
            answer.append(dic[base])

    return answer