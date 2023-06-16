/*
-- 1차 : 과거 값도 같이 출력 -> 최신상태만 남기기
SELECT DISTINCT(CAR_ID), 
(CASE 
    WHEN ('2022-10-16' BETWEEN START_DATE AND END_DATE) 
    THEN '대여중'
    ELSE '대여 가능'
    END) AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
ORDER BY CAR_ID DESC;

-- 2차 : GROUP BY 했을 때 첫번째 값이 남으니 역순으로 만들어 최신값만 보기
SELECT CAR_ID,
(CASE 
    WHEN ('2022-10-16' BETWEEN START_DATE AND END_DATE) 
    THEN '대여중'
    ELSE '대여 가능'
    END) AS AVAILABILITY
FROM (SELECT * 
      FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
      ORDER BY END_DATE DESC
      LIMIT 123456789) AS C
GROUP BY CAR_ID
ORDER BY CAR_ID DESC;
*/
-- 3차 : 힌트에서 MAX 활용 
SELECT CAR_ID, 
--  MAX(IF ('2022-10-16' BETWEEN START_DATE AND END_DATE, '대여중', '대여 가능')) AS AVAILABILITY
(CASE 
    WHEN MAX('2022-10-16' BETWEEN START_DATE AND END_DATE) THEN '대여중'
    ELSE '대여 가능'
    END) AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
ORDER BY CAR_ID DESC;
