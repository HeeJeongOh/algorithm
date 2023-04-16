'''
[시도1] 테케 통과 X
1. people 리스트 오름차순 정렬
2. 무게를 더해가며 무게합 >= limit일 때, answer++, 무게합 리셋

[시도2] 정확성: 20.0 + 효율성: 10.0 = 합계: 30.0 / 100.0
1. 탐욕법 유형 확인 -> 이중포문 작성
2. 어.. 왜 안되는거지 -> while 문 수정 
    for i in range(l):
        for j in range(i+1, l+1):
            print(people[i:j])
            if sum(people[i:j]) >= limit:
                answer += 1
                i = j
[시도3] 정확성: 75.0 + 효율성: 20.0 = 합계: 95.0 / 100.0
(HINT) "최대 2명씩 밖에 탈 수 없고" 문제 놓침.
1. 가장 무거운 사람(H)과 가벼운 사람(L)을 함께 태우는 것이 효율적
    1.1. H + L > limit : H 혼자 태우기

[시도4] 
(HINT) pop하는 과정에서 시간 복잡도 증가
 ㄴ i번째 리스트 원소를 제거하는 작업은 O(N)의 시간복잡도
1. 무거운 애 인덱스 hp, 가벼운 애 인덱스 lp
2. while문 조건 : lp <= hp

'''
def solution(people, limit):
    answer = 0
    people = sorted(people)
    hp = len(people)-1
    lp = 0
    print(people)
    while lp <= hp:
        print(lp, hp)
        if (people[lp] + people[hp]) > limit:
            hp -= 1
        else:
            lp += 1
            hp -= 1
            
        answer += 1

    return answer