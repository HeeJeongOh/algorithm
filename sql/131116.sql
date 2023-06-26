/*
-- 1차 : 문법 오류
SELECT CONCAT('/home/grep/src/',BOARD_ID,'/',FILE_ID, FILE_NAME, FILE_EXT) AS FILE_PATH
FROM (SELECT BOARD_ID FROM USED_GOODS_BOARD 
      ORDER BY VIEWS LIMIT 1) B, USED_GOODS_FILE
ON B.BOARD_ID = BOARD_ID;
*/
-- 2차 : 질문하기 참고
SELECT CONCAT('/home/grep/src/',BOARD_ID,'/',FILE_ID,FILE_NAME,FILE_EXT) AS FILE_PATH
FROM USED_GOODS_FILE
WHERE BOARD_ID = (SELECT BOARD_ID
                     FROM USED_GOODS_BOARD
                 ORDER BY VIEWS DESC LIMIT 1)
ORDER BY FILE_ID DESC;