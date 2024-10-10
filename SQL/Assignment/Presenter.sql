SELECT
    m.username,
    m.firstname,
    m.age
FROM
    memberinfo m
    INNER JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
    INNER JOIN diseasedetail d ON d.cardiodiagnosis_cardio_id = c.cardio_id;

-- Retrieve the xray records for
-- members who have a
-- cardiostress issue
-- (from cardiodiagnosis).
SELECT
    m.username,
    c.cardioarrestdetected,
    x.*
FROM
    memberinfo m
    INNER JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
    INNER JOIN xray x ON c.cardio_id = x.cardiodiagnosis_cardio_id
WHERE
    c.cardioarrestdetected = 1;