SELECT U.USER_ID, U.NICKNAME, 
    CONCAT(U.CITY, ' ', U.STREET_ADDRESS1, ' ', U.STREET_ADDRESS2) AS '전체주소', 
    CONCAT(LEFT(U.TLNO, 3), '-', MID(U.TLNO, 4, 4), '-', RIGHT(U.TLNO,4)) AS '전화번호'
FROM USED_GOODS_BOARD B JOIN USED_GOODS_USER U
ON B.WRITER_ID = U.USER_ID
GROUP BY B.WRITER_ID
HAVING COUNT(B.BOARD_ID) >= 3
ORDER BY U.USER_ID DESC;

/* 다른 사람 풀이 
select user_id, nickname, 
    concat(city, ' ', street_address1, ' ', street_address2) '전체주소',
    concat(left(tlno, 3), '-', mid(tlno, 4, 4), '-', substr(tlno,8)) '전화번호'
from used_goods_user
where user_id in (select writer_id
        from used_goods_board
        group by writer_id
        having count(writer_id) >= 3)
order by user_id desc;
*/