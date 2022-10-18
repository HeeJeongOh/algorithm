'''
0. 처음에 문제를 잘못읽어 모두 할인받을 수 있는 첫 날짜 반환
1. 50.0 -> 시간초과
    ㄴ 10개씩 확인하는 것이 무리인듯
2. 91.7 -> 실패 tc 11
    ㄴ '질문하기' 확인 -> 무슨 말인지 이해 못함.
    ㄴ 원인 : discount의 길이가 10일때 처리 X
'''
def solution(want, number, discount):
    # 모두 할인 받을 수 있는 회원등록 날짜의 총 일 수
    answer = 0
    
    # 애초에 원하는 제품이 없는 경우, 바로 return 0
    tmp = {w: discount.count(w) for w in want}
    if sum(tmp.values()) == 0:
        return 0
    
    ten_discount = discount[:10]
    records = {w: ten_discount.count(w) for w in want}    
            
    for d in range(10, len(discount)):       
        
        # print(records)
        # print(ten_discount)
        
        if list(records.values()) == number: 
            answer += 1

        # 10일씩 확인하기 - 삭제 후 추가
        if ten_discount[0] in want:
            records[ten_discount[0]] -= 1
        ten_discount.pop(0)
        
        ten_discount.append(discount[d])
        if ten_discount[-1] in want:
            records[ten_discount[-1]] += 1
            
    if list(records.values()) == number: 
            answer += 1    

    return answer