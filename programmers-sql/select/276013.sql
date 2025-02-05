-- Python 개발자 찾기
-- https://school.programmers.co.kr/learn/courses/30/lessons/276013

SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPER_INFOS
WHERE SKILL_1 = 'PYTHON'
   OR SKILL_2 = 'PYTHON'
   OR SKILL_3 = 'PYTHON'
ORDER BY ID;
