-- 특정 물고기를 잡은 총 수 구하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/298518

SELECT COUNT(*) AS FISH_COUNT
FROM FISH_INFO AS A
         JOIN FISH_NAME_INFO AS B
              ON A.FISH_TYPE = B.FISH_TYPE
WHERE FISH_NAME IN ('BASS', 'SNAPPER');