'''
1. std를 기준으로 std 뒤에 있는 숫자들 모두 확인 -- 82.6 (시간초과)
2. 예외처리를 위해 if문 삽입 시, 오히려 더 이른 시간초과 발생

3. 힌트: stack 활용
    3.1. 뒤에서부터 읽어오기
    3.2. 스택에 현재 값 기준 큰 값들을 넣기
    3.3. 스택에서 뒤 쪽에 위치할수록 나와 가까운 것.
4. 줄세우기로 생각하면 이해가 훨씬 쉬움
		4.1 내 뒤에 있는 애들 중 다음으로 키 큰 애 찾기
		4.2 어차피 나보다 작은 애는 앞에서 안 보이니까 스택에서 없애는 것
		4.3 새로운 최댓값 등장 시 어차피 뒤에 애들 안 보이니까 리셋.
'''
def solution(numbers):
    answer = []
    stack = []
    nmax = -1
    for n in numbers[::-1]:
        # 나보다 큰 값을 만나면 스택 초기화 및 최댓값 변경
        if n >= nmax:
            stack = [n]
            nmax = n
            answer.append(-1)
        # 나와 같거나 작은 값을 만나면
        else:
            # 스택에 있는 값을 비교해가면서
            for s in stack[::-1]:
                # 나와 가장 가까이 있는 큰 수 찾기
                if s > n:
                    answer.append(s)
                    break
                # 나보다 작은 값은 제거하기
                else:
                    stack.pop()
            # 큰 수 층 쌓기
            stack.append(n)
            
    # 반대로 정렬하여 출력
    return answer[::-1]
