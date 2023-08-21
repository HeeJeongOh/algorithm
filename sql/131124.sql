-- 리뷰 개수가 최대인 사람 중 1명 출력
SELECT M.MEMBER_NAME, R.REVIEW_TEXT, DATE_FORMAT(R.REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
FROM MEMBER_PROFILE M JOIN REST_REVIEW R USING (MEMBER_ID)
WHERE R.MEMBER_ID = (SELECT MEMBER_ID
                    FROM REST_REVIEW
                    GROUP BY MEMBER_ID
                    ORDER BY COUNT(MEMBER_ID) DESC
                    LIMIT 1)
ORDER BY 3,2;

-- 리뷰 개수가 최대인 사람 모두 출력
SELECT M.MEMBER_NAME, R.REVIEW_TEXT, DATE_FORMAT(R.REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
FROM MEMBER_PROFILE M JOIN REST_REVIEW R USING (MEMBER_ID)
-- 리뷰를 가장 많이 작성한 회원들 선택
WHERE MEMBER_ID IN (SELECT MEMBER_ID FROM REST_REVIEW 
                    GROUP BY MEMBER_ID
	                  -- 가장 많이 작성된 리뷰 수
										HAVING COUNT(*) = (SELECT COUNT(*) FROM REST_REVIEW
									                     GROUP BY MEMBER_ID
									                     ORDER BY COUNT(*) DESC LIMIT 1)
                   )
ORDER BY 3, 2;