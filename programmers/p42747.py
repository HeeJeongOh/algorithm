'''
[시도1]
1. h를 1씩 늘려가면서 확인하기
2. h번 이상 인용된 논문이 h편 이상인가
3. 그 외 논문이 h번 이하로 인용되었는가

[시도2] h-index 검색 : https://postechlibrary.tistory.com/489
1. 내림차순 정렬
2. 인용횟수 >= 순위 
'''
def solution(citations):
    answer = 0
    citations = sorted(citations, reverse=True)
    for i in range(len(citations)):
        if citations[i] >= (i+1):
            answer = (i+1)
    
    return answer
