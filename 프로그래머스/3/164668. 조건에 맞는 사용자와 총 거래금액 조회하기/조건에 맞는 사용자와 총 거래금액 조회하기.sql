-- 완료된 중고 거래의 총금액이 70만원 이상인 사람의 회원 정보, 총 거래 금액 조회
SELECT U.USER_ID, U.NICKNAME, SUM(PRICE) AS TOTAL_SALES
FROM USED_GOODS_BOARD B LEFT JOIN USED_GOODS_USER U
ON B.WRITER_ID = U.USER_ID
WHERE STATUS = "DONE"
GROUP BY WRITER_ID
HAVING SUM(PRICE) >= 700000
ORDER BY 3;