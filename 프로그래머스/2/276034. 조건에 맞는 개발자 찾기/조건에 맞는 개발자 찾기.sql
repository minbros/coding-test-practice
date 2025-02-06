select distinct(d.ID), d.EMAIL, d.FIRST_NAME, d.LAST_NAME
from DEVELOPERS d
join SKILLCODES s on d.SKILL_CODE & s.CODE
where s.NAME = 'C#'
    or s.NAME = 'Python'
order by ID;