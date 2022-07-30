# 윤년 : 2월이 29일까지 존재
def solution(a, b):
    cal = {30: [4, 6, 9, 11], 
           29: [2]}
    days = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    # 2016년 1월 1일은 금요일
    d = b
    for i in range(1, a):
        if i == 2:
            d += 29
        elif i == 4 or i == 6 or i == 9 or i == 11:
            d += 30
        else:
            d += 31
    return days[d%7-1]

print(solution(a=5, b=4))