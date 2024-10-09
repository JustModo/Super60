SELECT
    *
FROM
    memberinfo m
WHERE
    m.age > 30
    AND m.age < 50;

SELECT
    AVG(b.bloodpressure)
from
    bloodtest b;

SELECT
    *
FROM
    cardiodiagnosis c
ORDER BY
    c.cardioarrestdetected DESC,
    c.date DESC;

SELECT
    m.username,
    m.firstname,
    d.disease_id
from
    memberinfo m
    INNER JOIN cardiodiagnosis c on m.member_id = c.memberinfo_member_id
    INNER JOIN diseasedetail d ON c.cardio_id = d.cardiodiagnosis_cardio_id;

SELECT
    m.username,
    m.age,
    a.country
FROM
    memberinfo m
    INNER JOIN addressinfo a ON m.member_id = a.memberinfo_member_id
WHERE
    m.age > 40
GROUP BY
    a.country;