'''
1. 약수 구하기 -> 시간초과
    for i in range(1, num+1):
        if num % i == 0:
            cnt += 1
2. range를 절반으로 -> 제곱수 처리 해주기
3. dp로 약수 구해나가기 /  소인수분해
'''

def get_div(num):
    cnt = 0
    for i in range(1, int(num**(1/2))+1):
        if num % i == 0: 
            if i**2 == num:
                cnt += 1
                break
            else:
                cnt += 2
    return cnt

def solution(number, limit, power):
    counts = []
    for n in range(1, number+1):
        c = get_div(n)
        if c > limit:
            counts.append(power)
        else:
            counts.append(c)
    return sum(counts)
