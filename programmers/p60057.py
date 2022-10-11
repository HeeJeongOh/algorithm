# 아이디어는 냈으나 코드 구현은 구글링
# i개(기준 문자열) 단위로 잘라 압축하기
def solution(s):
    answer = len(s)
    # len(s) // 2 + 1 인 이유 : 최소 길이 전체 길이가 반이 되는 경우
    for i in range(1, len(s)//2 + 1):
        tmp = ""
        idx = 0
        while idx < len(s):
            std = s[idx:idx+i]  # 기준 문자열
            cnt = 1             # 기준 문자열의 개수 
            
            # 해당 기준 문자열이 연달아 나오는 개수 세기
            while std == s[idx+i: idx+i+i]:
                idx += i
                cnt += 1
            
            # abab -> 2ab 형태로 tmp에 더하기, 개수가 1인 경우 그냥 더하기 
            tmp += (str(cnt) + std) if cnt != 1 else std
            idx += i

        # 길이가 더 짧다면 업데이트
        answer = len(tmp) if len(tmp) < answer else answer

    return answer

print(solution('ababcdcdababcdcd'))