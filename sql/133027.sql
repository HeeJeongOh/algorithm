/*-- 1차 : TOTAL을 출력하지 않는 방법을 모르겠음
SELECT FLAVOR, (J.TOTAL_ORDER + F.TOTAL_ORDER) AS TOTAL
FROM (SELECT * FROM JULY
     GROUP BY FLAVOR
     HAVING SUM(TOTAL_ORDER))  J
     JOIN 
     (SELECT * FROM FIRST_HALF
     GROUP BY FLAVOR
     HAVING SUM(TOTAL_ORDER)) F USING (FLAVOR) 
ORDER BY (J.TOTAL_ORDER + F.TOTAL_ORDER) DESC
LIMIT 3;
*/

-- 2차 : HAVING절을 ORDER BY 내에 작성한것일까
SELECT FLAVOR
FROM JULY J JOIN FIRST_HALF F USING (FLAVOR)
GROUP BY FLAVOR
ORDER BY (SUM(J.TOTAL_ORDER) + SUM(F.TOTAL_ORDER)) DESC
LIMIT 3;