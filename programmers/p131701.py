'''
원형수열 : 처음과 끝이 연결되어 있는 수열
원형 수열의 연속 부분 수열 합 구하기
def solution(elements):
    length = len(elements)
    elements += elements
    print(elements)
    nums = []
    # 길이를 기준으로 부분수열 합 구하기
    for l in range(1, length+1):
        for i in range(length):
            nums.append(sum(elements[i:i+l]))
    return len(set(nums))

-- 230616
1. 길이=i를 하나씩 늘려가면서 더하기
    1.1 시작 인덱스가 다시 0으로 돌아오면 길이 늘리기
2. 길이가 1일 때, 전체 길이일 때는 미리 더해두기
3. 나머지로 할까 늘릴까 고민하다가 그냥 늘리는 게 덜 헷갈려서 그거 선택함
'''
def solution(elements):
    answer = elements.copy()
    answer += [sum(elements)]
        
    # 원형수열을 표현하기 위해 확장
    size = len(elements)
    elements += elements
    for i in range(2, size):
        for j in range(size):
            answer.append(sum(elements[j:j+i]))
    return len(set(answer))