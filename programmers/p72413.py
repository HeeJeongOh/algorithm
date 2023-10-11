'''
[질문하기]
1. A와 B를 둘 다 정렬
2. B배열의 제일 작은 원소가 A배열의 제일 작은 원소를 못이긴다면, 
	 그 B배열의 원소는 더 이상 필요없을 것이다
3. 결국 이길 수 있는 b 원소의 개수를 세는 것.
'''
def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    '''
    # 아래 코드는 a와 b가 나란히 검토됨
    for a, b in zip(A, B):
        if a < b:
            answer += 1
    '''
    while B:
        if A[0] < B[0]:
            answer += 1
            A.pop(0)
        B.pop(0)
    return answer

'''
[시도4]
1. 점수 매기기 부분 간결하게
    b = list(cands.values())
    return len(b) - b.count(1000000000)
2. 1000000000 카운트 제거
    if문 내부에 answer += 1 추가
3. cands를 제거
4. visited 대신 B pop ? visited가 더 빠를 것 같지만 일단 시도
5. if문 조건확인 순서 변경... 

def solution(A, B):
    answer = 0
    B.sort()
    visited = {b: 1 for b in B}
    for a in A:
        tmp = 1000000000
        for b in B:           
            if  visited[b] and b < tmp and b > a:
                tmp = b
                visited[b] = 0
                answer += 1
    return (answer)

    
[시도3] 시간초과 3 (85.7 / 100.0)
1. 처음부터 후보 a를 이길 수 있는b 지정
2. 사용한 b에 대해 기록 남기기

def solution(A, B):
    answer = 0
    B.sort()
    cands = {a: 1000000000 for a in A}
    visited = {b: 1 for b in B}
    for a in A:
        for b in B:           
            if b > a and b < cands[a] and visited[b]:
                cands[a] = b
                visited[b] = 0
    # print(cands)
    for c, a in zip(cands, A):
        if cands[c] != 1000000000:
            answer += 1
       
    return (answer)

[시도2] 시간초과 5 시간초과 3, (61.9 / 100.0)
1. b가 a를 이길 수 있는 경우 만들기
2. 해당 경우 중 작은 b부터 이용
3. 최종 점수 매길 때 사용한 b 제거

def solution(A, B):
    answer = 0
    B.sort()
    cands = {a: [] for a in A}
    for a in A:
        for b in B:
            if b > a:
                cands[a] += [b]
    for c, a in zip(cands, A):
        if cands[c]:
            answer += 1

            b = cands[c][0]
            for c in cands:
                if b in cands[c]:
                    cands[c].remove(b)              
    return (answer)

[시도1]
0. a팀 출전순서를 보고 최대 승점을 구할 수 있는 방법
[시도1] 전체 시간초과
1. b의 출전 경우의 수 모두 구해서 경쟁해보기 ? -> 시간초과 예상

from itertools import permutations
def solution(A, B):
    answer = [0]
    for b in set(permutations(B, len(B))):
        cnt = 0
        for aa, bb in zip(A, b):
            if aa < bb:
                cnt += 1
        answer += [cnt]
    return max(answer)
'''