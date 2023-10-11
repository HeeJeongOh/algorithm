'''
[시도1] 실패 5
1. 두 글자씩 끊어서 다중집합의 원소로 만들기
    1.1 영문자로 된 글자 쌍만 유효
    1.2 대소문자 구분 x
2. J(A, B) = 두 집합의 교집합 크기 / 두 집합의 합집합 크기
3. 실제로 set을 이용하면 예제3 통과 x : 중복허용
    3.1 예제 {1, 1} {1, 1, 1, 1, 1} 적용
    3.2 예제 {1, 1, 2, 2, 3} {1, 1, 2, 2, 3, 4, 5} 미적용
    
def reassemble(word):
    tmp = []
    for i in range(len(word)):
        if word[i:i+2].isalpha() and len(word[i:i+2]) == 2:
            tmp.append(word[i:i+2].lower())
    return tmp

def solution(str1, str2):
    answer = 0
    list1, list2 = reassemble(str1), reassemble(str2)

    if sorted(list1) == sorted(list2):
        answer = 1
    else:
        set1, set2 = set(list1), set(list2)
        # {1, 1} {1, 1, 1}
        if set1 == set2:
            answer = min(len(list1), len(list2)) / max(len(list1), len(list2))
        else:
            answer = len(set1.intersection(set2)) / len(set1.union(set2))
    return int(answer * 65536)
'''
'''
[시도2]
1. inter과 union 구하는 방식 변경
2. union = A + B - A&B
3. inter : 직접 하나씩 지우기
'''
def reassemble(word):
    tmp = []
    for i in range(len(word)):
        if word[i:i+2].isalpha() and len(word[i:i+2]) == 2:
            tmp.append(word[i:i+2].lower())
    return tmp

def solution(str1, str2):
    answer = 0
    list1, list2 = reassemble(str1), reassemble(str2)
    # print(list1, list2)
    if sorted(list1) == sorted(list2):
        answer = 1
    else:
        inter = 0
        tmp2 = list2.copy()
        for l1 in list1:
            if l1 in tmp2:
                tmp2.remove(l1)
                inter += 1
        union = len(list1) + len(list2) - inter
        
        # print(inter, union)
        answer = inter / union
    return int(answer*65536)