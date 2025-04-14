-- 10
CREATE VIEW xray_with_memberinfo AS
SELECT
    x.*,
    m.*
FROM
    xray AS x
    INNER JOIN cardiodiagnosis AS c ON x.cardiodiagnosis_cardio_id = c.cardio_id
    INNER JOIN memberinfo AS m ON c.memberinfo_member_id = m.member_id;

SELECT
    *
FROM
    xray_with_memberinfo;

-- 11
CREATE VIEW latest_diseasedetail AS
SELECT
    *
FROM
    diseasedetail
ORDER BY
    diagnoseddate DESC;

SELECT
    *
FROM
    latest_diseasedetail;

-- 12
CREATE VIEW average_bg_by_id AS
SELECT
    b.bloodpressure,
    m.member_id,
    m.firstname,
    m.lastname
FROM
    bloodtest b
    INNER JOIN cardiodiagnosis c ON b.cardiodiagnosis_cardio_id = c.cardio_id
    INNER JOIN memberinfo m ON m.member_id = c.memberinfo_member_id
SELECT
    *
FROM
    average_bg_by_id;

-- ABISHAA
-- 1. Create a view to get member details with their address.
create VIEW member_address_view as
SELECT
    m.member_id,
    m.firstname,
    m.lastname,
    a.city,
    a.state,
    a.country
from
    memberinfo m
    INNER join addressinfo a on m.member_id = a.memberinfo_member_id;

SELECT
    *
FROM
    member_address_view;

-- 2. Write a view to get cardio diagnosis details along with member names.
CREATE view member_cardio_details as
SELECT
    m.member_id,
    m.firstname,
    c.cardio_id,
    c.cardioarrestdetected,
    c.date
from
    memberinfo m
    INNER join cardiodiagnosis c on m.member_id = c.memberinfo_member_id
SELECT
    *
from
    member_cardio_details;

-- 3. Create a view to display disease details along with recovery status.
create view recovery_status as
SELECT
    d.disease_id,
    d.diagnoseddate,
    d.recovereddate,
    d.isrecovered,
    d.cardiodiagnosis_cardio_id
from
    diseasedetail d
SELECT
    *
from
    recovery_status;

-- 14
CREATE VIEW ecg_vs_bp AS
SELECT
    b.*,
    e.restecg
from
    bloodtest b
    INNER JOIN cardiodiagnosis c ON b.cardiodiagnosis_cardio_id = c.cardio_id
    INNER JOIN ecgreport e ON e.cardiodiagnosis_cardio_id = c.cardio_id