SELECT T.AUTHOR_ID, T.AUTHOR_NAME, T.CATEGORY, SUM(T.PRICE * S.SALES) AS TOTAL_SALES
FROM (SELECT B.BOOK_ID, A.AUTHOR_ID, A.AUTHOR_NAME, B.CATEGORY, B.PRICE
FROM AUTHOR AS A
JOIN BOOK AS B ON A.AUTHOR_ID = B.AUTHOR_ID) AS T
JOIN (SELECT BOOK_ID, SUM(SALES) AS SALES
FROM BOOK_SALES
WHERE SALES_DATE LIKE '2022-01-%'
GROUP BY BOOK_ID) AS S
ON T.BOOK_ID = S.BOOK_ID
GROUP BY T.AUTHOR_ID, T.AUTHOR_NAME, T.CATEGORY
ORDER BY AUTHOR_ID, CATEGORY DESC;