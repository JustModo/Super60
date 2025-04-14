SELECT
    COUNT(*)
from
    memberinfo;

-- Simple Store Procedure
CREATE PROCEDURE get_member_count () BEGIN
SELECT
    COUNT(*)
from
    memberinfo;

END;

CALL get_member_count ();

-- age >40
SELECT
    COUNT(*)
FROM
    memberinfo
where
    age > 40;

-- Procedure
CREATE PROCEDURE get_member_count_by_age (member_age int) BEGIN
SELECT
    COUNT(*)
FROM
    memberinfo
where
    age > member_age;

END;

CREATE PROCEDURE get_member_info_by_id (IN member_id_param VARCHAR(10)) BEGIN
SELECT
    *
FROM
    memberinfo
WHERE
    member_id = member_id_param;

END;

CALL get_member_info_by_id ("M100") CREATE PROCEDURE get_member_countByAge (
    IN member_age INT,
    OUT member_count INT
) BEGIN
SELECT
    COUNT(*) INTO member_count
FROM
    memberinfo
WHERE
    age > member_age;

END
SET
    @member_count = 0;

CALL get_member_countByAge (30, @member_count);

SELECT
    @member_count;

-- Get all members
CREATE PROCEDURE get_all_members() BEGIN
SELECT
    *
FROM
    memberinfo;

END CALL get_all_members;

CREATE PROCEDURE get_member_by_gender(IN member_gender int) BEGIN
SELECT
    *
from
    memberinfo
WHERE
    age = member_gender;

END CALL get_member_by_gender (1);

CREATE PROCEDURE get_member_by_gender_age(IN member_gender int, IN member_age int) BEGIN
SELECT
    *
FROM
    memberinfo
WHERE
    gender = member_gender
    and age = member_age;

END CALL get_member_by_gender_age (1, 30) CREATE PROCEDURE get_member_count_using_with (
    IN member_gender int,
    IN member_age int
) BEGIN WITH filtered_members AS (
    SELECT
        *
    FROM
        memberinfo
    WHERE
        gender = member_gender
        AND age = member_age
)
SELECT
    *
FROM
    filtered_members;

END DROP PROCEDURE get_member_count_using_with CALL get_member_count_using_with (1, 30);


