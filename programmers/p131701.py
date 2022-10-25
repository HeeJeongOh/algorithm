'''
원형수열 : 처음과 끝이 연결되어 있는 수열
원형 수열의 연속 부분 수열 합 구하기
'''
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

e = [7,9,1,1,4]	
ans = 18

print(solution(e))