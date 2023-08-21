/*
1번. 자동차 종류가 '세단' 또는 'SUV' 인 자동차
2번. 2022년 11월 1일부터 2022년 11월 30일까지 대여 가능
3번. 30일간의 대여 금액이 50만원 이상 200만원 미만인 자동차
4번. 대여 금액 내림차순, 자동차 종류 오름차순, 자동차 ID 내림차순 정렬
*/

# 아래 조건들에 의해 이미 각 차량에 대한 DAILY_FEE, DISCOUNT_RATE 매칭 
SELECT C.CAR_ID, C.CAR_TYPE, TRUNCATE(C.DAILY_FEE*(100-DISCOUNT_RATE)/100*30,0) AS FEE
# 모든 테이블을 합치기
FROM CAR_RENTAL_COMPANY_CAR C
    INNER JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY H USING (CAR_ID)
    INNER JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN P USING (CAR_TYPE)
# 1번                              # 2번
WHERE C.CAR_TYPE IN ('세단','SUV') AND P.DURATION_TYPE = '30일 이상'
# 같은 차량, 다른 대여 기록에 대한 처리
GROUP BY C.CAR_ID
# 2번 : 11월 1일전에 대여가 끝나야 함        # 3번 
HAVING (MAX(END_DATE) < '2022-11-01') AND FEE BETWEEN 500000 AND 2000000
# 4번 
ORDER BY 3 DESC, 2 ASC, 1 DESC;