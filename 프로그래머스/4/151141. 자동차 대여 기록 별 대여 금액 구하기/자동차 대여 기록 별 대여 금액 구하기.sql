SELECT HISTORY_ID, ROUND((100 - DISCOUNT_RATE) * DAILY_FEE * DURATION / 100) AS FEE
FROM (
    SELECT T.*, IFNULL(P.DISCOUNT_RATE, 0) AS DISCOUNT_RATE
    FROM (
        SELECT H.HISTORY_ID, H.CAR_ID, 
        DATEDIFF(H.END_DATE, H.START_DATE) + 1 AS DURATION,
        CASE WHEN DATEDIFF(H.END_DATE, H.START_DATE) + 1 >= 90 THEN '90일 이상'
        WHEN DATEDIFF(H.END_DATE, H.START_DATE) + 1 >= 30 THEN '30일 이상'
        WHEN DATEDIFF(H.END_DATE, H.START_DATE) + 1 >= 7 THEN '7일 이상'
        ELSE '7일 미만' END AS DURATION_TYPE,
        C.CAR_TYPE, C.DAILY_FEE
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY AS H
        JOIN CAR_RENTAL_COMPANY_CAR AS C
        ON H.CAR_ID = C.CAR_ID
        WHERE CAR_TYPE = '트럭'
    ) AS T
    LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN AS P
    ON T.CAR_TYPE = P.CAR_TYPE AND T.DURATION_TYPE = P.DURATION_TYPE
) AS P
ORDER BY FEE DESC, HISTORY_ID DESC;