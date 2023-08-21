- ⁉️ **대여 횟수가 많은 자동차들의 월별 대여 횟수 구하기**
    
    ```sql
    -- 1차
    SELECT MONTH(C.START_DATE) AS MONTH, C.CAR_ID, COUNT(C.CAR_ID) AS RECORDS
    FROM (SELECT * FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
          WHERE START_DATE BETWEEN '2022-08-01' AND '2022-10-31') AS C
    GROUP BY C.CAR_ID HAVING RECORDS >= 5 
    ORDER BY MONTH ASC, C.CAR_ID DESC;
    ```
    
    ```sql
    -- 2차 
    SELECT MONTH(START_DATE) AS MONTH, CAR_ID, COUNT(*) AS RECORDS
    FROM (
        SELECT *
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
        WHERE START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
        GROUP BY CAR_ID) H
    GROUP BY MONTH, CAR_ID
    ORDER BY MONTH, CAR_ID DESC;
    ```
    
    ```sql
    -- 3차 : 
    SELECT MONTH(START_DATE) AS MONTH, CAR_ID, COUNT(*) AS RECORDS
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    -- 날짜에 대한 필터링을 한 번 더 하는 이유 : ??
    WHERE START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
        AND CAR_ID IN 
        -- 대여 시작일을 기준으로 2022년 8월부터 2022년 10월까지 총 대여 횟수가 5회 이상인 자동차들
        (SELECT CAR_ID
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
        WHERE START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
        GROUP BY CAR_ID
        HAVING COUNT(*) >= 5)
    GROUP BY MONTH, CAR_ID
    ORDER BY MONTH, CAR_ID DESC;
    ```