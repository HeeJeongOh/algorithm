-- 공간을 둘 이상 등록한 사람에 대해 공간의 정보를 아이디 순으로 조회

SELECT *
FROM PLACES P
WHERE HOST_ID IN (SELECT HOST_ID
            FROM PLACES
            GROUP BY HOST_ID
            HAVING COUNT(ID) >= 2)
ORDER BY ID;