'''
ee = [(1, a), (0, b), (3, d)(5, c), (2, a)]
# sorted - 원본 데이터 변경 o, 정렬된 결과 반환
r1 = sorted(ee)                      # 1번째 값에 대해 정렬
r2 = sorted(ee, key=lambda x:x[1])   # 2번째 값에 대해 정렬
# sort - 원본 데이터 변경 o, 반환값 x
ee.sort(key=lambda x: x[1])         
'''
def solution(strings, n):
    answer = sorted(strings, key=lambda x:(x[n], x))
    return answer

print(solution(["abce", "abcd", "cdx"], 2))