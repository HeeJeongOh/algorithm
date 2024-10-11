-- 아직 입양을 못 간 동물들 중, 가장 오래 보호소에 있었던 동물 3마리의 이름과 보호시작일 조회
SELECT NAME, DATETIME
FROM ANIMAL_INS
WHERE ANIMAL_ID NOT IN (SELECT ANIMAL_ID
                       FROM ANIMAL_OUTS)
ORDER BY DATETIME ASC
LIMIT 3;
