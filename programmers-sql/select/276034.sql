-- 조건에 맞는 개발자 찾기
-- https://school.programmers.co.kr/learn/courses/30/lessons/276034

SELECT DISTINCT(D.ID), D.EMAIL, D.FIRST_NAME, D.LAST_NAME
FROM DEVELOPERS AS D
JOIN SKILLCODES AS S ON D.SKILL_CODE & S.CODE != 0
WHERE S.NAME = 'C#' OR S.NAME = 'Python'
ORDER BY ID;