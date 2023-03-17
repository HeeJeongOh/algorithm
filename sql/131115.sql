-- SUCCESS

SELECT *
FROM FOOD_PRODUCT
ORDER BY PRICE DESC
LIMIT 1;

/* 다른 답안 
select *
from food_product
where price = (SELECT max(price) as price from food_product);
*/