from collections import defaultdict
import math
from datetime import datetime

def getMinutes(start, end):
    # start = '12:34' / end = '13:32'
    mm = 0
    st = datetime.strptime(start, '%H:%M')
    en = datetime.strptime(end, '%H:%M')

    mm = (en-st).seconds/60

    return mm

def solution(fees, records):
    # {차량번호 : [입차, 출차, [주차시간1, 주차시간2, ...]]}
    car_table = defaultdict(lambda: ['00:00', '23:59', 0])
    answer = []

    # 자동차별 누적주차시간 표 만들기
    for r in records:
        time, car, state = r.split(' ')
        if state == 'IN':
            car_table[car][0] = time
        elif state == 'OUT':
            # 주차시간 계산
            car_table[car][1] = time
            mm = getMinutes(car_table[car][0], car_table[car][1])
            car_table[car][2] += mm

            # 다시 입출차 초기화
            car_table[car][0], car_table[car][1] = '23:59', '23:59'

    # 차량 번호가 작은 자동차부터 청구할 주차 요금을 차례대로 정수 배열에 담아서 return
    car_table = sorted(car_table.items())
    # 각 차량에 대한 누적 주차 요금 구하기
    # fee = 기본 시간(분), 기본 요금(원), 단위 시간(분), 단위 요금(원)
    for car_info in car_table:
        if car_info[1][0] != '23:59' and car_info[1][1] == '23:59':
            car_info[1][2] += getMinutes(car_info[1][0], car_info[1][1])
        
        print(car_info)

        times = car_info[1][2]
        if times < fees[0]:
            answer.append(fees[1])
        else:
            answer.append(math.ceil((times-fees[0])/fees[2])*fees[3] + fees[1] )
    
    return answer

f = [180, 5000, 10, 600]
r = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(f,r))

print()
ff = [1, 461, 1, 10]
rr = ["00:00 1234 IN"]
print(solution(ff,rr))
