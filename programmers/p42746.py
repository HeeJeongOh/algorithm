'''
[시도1] 33.3 / 100.0
1. 숫자의 첫번째 문자가 큰 순으로 정렬하여 이어 붙이기
2. i번째가 같다면 i+1이 큰 숫자로 이어 붙이기
3. 해시 활용하여 순서 내림차순 정렬
    
[시도2] 53.3 / 100.0
ㄴ 테스트2 : 30과 3의 순서 설정: 34 3 30 > 34 30 3 
1. permutations 시도 -> 시간초과
    from itertools import permutations
    def solution(numbers):
        ans = ''
        numbers = [str(n) for n in numbers]
        hm = {str(i): [] for i in range(10)}
        for n in numbers:
            hm[n[0]].append(n)

        for key in range(9, -1, -1):
            tmp = sorted(hm[str(key)], reverse=True)
            if len(tmp) > 1:
                # tmp 순서 컴비네이션
                cases = []
                for nums in permutations(tmp, len(tmp)):
                    cases.append("".join(nums))
                ans += max(cases)
            else:   
                ans += "".join(tmp)
        return ans

[시도3] (힌트확인) https://school.programmers.co.kr/questions/45680
1. numbers의 원소는 0 이상 1,000 이하 
	-> 모든 숫자를 4자릿수로 변경
2. 내림차순 정렬 후 이어붙이기
'''
def solution(numbers):
    ans = ''
    numbers = [str(n) for n in numbers]
    # 자릿수를 맞추어 비교 가능
    # 30 -> 3030
    # 3  -> 3333
    # 34 -> 3434
    numbers.sort(key=lambda x: (x * 4)[:4], reverse=True)
    ans = ''.join(numbers)

    return ans if ans[0] != '0' else '0'