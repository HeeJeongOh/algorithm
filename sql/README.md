### 쿼리 정리
- AVG(col) : 평균
- ROUND(col, 자릿수) : 반올림
- SELECT IF(500<1000, "YES", "NO") : 조건문
- DATEDIFF(date1, date2) : 날짜계산
- DATE에서 년월일 정보 추출 : YEAR(date), MONTH(date), DAY(date)
- DATE_FORMAT(date, '%Y-%m-%d') : 날짜 형식 수정
- SUBSTRING(문자열, start, end) / RIGHT(문자열, len) / LEFT(문자열, len) : 문자열 자르기 
- IFNULL(col, val) : NULL인 경우, 출력 변경
- AS : 선언의 경우 공백이 포함되는 경우, 작은 따옴표로 감싸기, 참조할 때에는 '' 필요 없음
- DIV : 나눗셈 연산 // 와 동일
- TABLE명 T : 해당 테이블의 컬럼 호출 시, T.컬럼명 사용
- HAVING : GROUP BY 사용 시, 집계함수를 통한 조건절 작성 시 사용
- MID/SUBSTR/SUBSTRING(문자열, start, len): 문자열서 start부터 len개 읽어오기
- col BETWEEN a AND b : A 이상 B 이하
- CASE (WHEN 조건 THEN 결과)* END AS col : case문
    ㄴ case when-then when-then else end