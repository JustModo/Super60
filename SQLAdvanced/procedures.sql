-- 2
CREATE PROCEDURE get_memberinfo() BEGIN
SELECT
    *
FROM
    memberinfo;

END;

CALL get_memberinfo();

-- 23
CREATE FUNCTION get_xray_count() RETURNS int BEGIN DECLARE result int;

SELECT
    COUNT(*) INTO result
FROM
    xray;

RETURN result;

END;

SELECT
    get_xray_count();

-- 1
CREATE PROCEDURE insert_into_membertable(
    IN member_id varchar(15),
    IN username varchar(15),
    IN firstname varchar(15),
    IN lastname varchar(15),
    IN age int,
    IN gender varchar(15),
    IN email varchar(15),
    IN phonenumber BIGINT
) BEGIN
INSERT INTO
    memberinfo (
        member_id,
        username,
        firstname,
        lastname,
        age,
        gender,
        email,
        phonenumber
    )
VALUES
    (
        member_id,
        username,
        firstname,
        lastname,
        age,
        gender,
        email,
        phonenumber
    );

END;

CALL insert_into_membertable(
    "M400",
    "hello",
    "Yash",
    "Laxman",
    20,
    "1",
    "abc@123",
    1234567890
);

-- 6
CREATE PROCEDURE insert_into_ecgtable(
    IN ecg_id varchar(15),
    IN date DATETIME,
    IN restecg INT,
    IN cardiodiagnosis_cardio_id VARCHAR(15)
) BEGIN
INSERT INTO
    ecgreport (
        ecg_id,
        date,
        restecg,
        cardiodiagnosis_cardio_id
    )
VALUES
    (
        ecg_id,
        date,
        restecg,
        cardiodiagnosis_cardio_id
    );

END;

CALL insert_into_ecgtable("ecgid400", "2019-01-24 00:00:00", 1, "cid122");

SELECT
    *
from
    ecgreport;

-- 7
CREATE PROCEDURE insert_into_wearabledevicetable(
    IN wearable_device_id VARCHAR(15),
    IN thalach INT,
    IN slope INT,
    IN date DATETIME,
    IN cardiodiagnosis_cardio_id VARCHAR(15)
) BEGIN
INSERT INTO
    wearabledevicedata (
        wearable_device_id,
        thalach,
        slope,
        date,
        cardiodiagnosis_cardio_id
    )
VALUES
    (
        wearable_device_id,
        thalach,
        slope,
        date,
        cardiodiagnosis_cardio_id
    );

END;

CALL insert_into_wearabledevicetable(
    "wd300",
    "160",
    1,
    "2019-01-24 00:00:00",
    "cid144"
);

-- 22
CREATE FUNCTION get_ecg_count() RETURNS int BEGIN DECLARE result int;

SELECT
    COUNT(*) INTO result
FROM
    ecgreport;

RETURN result;

END;

SELECT
    get_ecg_count();

-- 21
CREATE FUNCTION get_avg_bp() RETURNS int BEGIN DECLARE result int;

SELECT
    AVG(bloodpressure) INTO result
FROM
    bloodtest;

RETURN result;

END;

SELECT
    get_avg_bp();

-- 20
CREATE FUNCTION total_diagnosis_by_id(member_id varchar(15)) RETURNS int BEGIN DECLARE result int;

SELECT
    COUNT(*) INTO result
FROM
    cardiodiagnosis
WHERE
    memberinfo_member_id = member_id;

RETURN result;

END;

SELECT
    total_diagnosis_by_id("M3000");

-- 19
CREATE FUNCTION get_member_count() RETURNS int;

BEGIN;

DECLARE result int;

SELECT
    COUNT(*) INTO result
FROM
    memberinfo;

RETURN result;

END;

SELECT
    get_member_count();

-- 18
CREATE PROCEDURE get_xray_by_cid(IN cid VARCHAR(15)) BEGIN
SELECT
    *
FROM
    xray
WHERE
    cardiodiagnosis_cardio_id = cid;

END;

CALL get_xray_by_cid("cid122");

-- 17
CREATE PROCEDURE get_symptom_by_cid(IN cid VARCHAR(15)) BEGIN
SELECT
    *
FROM
    symptom
WHERE
    cardiodiagnosis_cardio_id = cid;

END;

CALL get_symptom_by_cid("cid122");

-- 16
CREATE PROCEDURE get_wearable_by_cid(IN cid VARCHAR(15)) BEGIN
SELECT
    *
FROM
    wearabledevicedata
WHERE
    cardiodiagnosis_cardio_id = cid;

END;

CALL get_wearable_by_cid("cid122");

--15 
CREATE PROCEDURE get_ecg_by_cid(IN cid VARCHAR(15)) BEGIN
SELECT
    *
FROM
    ecgreport
WHERE
    cardiodiagnosis_cardio_id = cid;

END;

CALL get_ecg_by_cid("cid122");

-- ABISHAA
-- 3.Write a stored procedure to insert an address for a member in the addressinfo table.
CREATE PROCEDURE get_member_address_info(
    IN address_id VARCHAR(15),
    IN member_id VARCHAR(15),
    IN city VARCHAR(15),
    IN state VARCHAR(20),
    IN country VARCHAR(20),
    IN pincode VARCHAR(20)
) BEGIN
INSERT INTO
    addressinfo (
        address_id,
        memberinfo_member_id,
        city,
        state,
        country,
        pincode
    )
VALUES
    (
        address_id,
        member_id,
        city,
        state,
        country,
        pincode
    );

END drop PROCEDURE get_member_address_info CALL get_member_address_info(
    'add101',
    'M100',
    'Mangalore',
    'Karnataka',
    'India',
    '5425-2154'
)
SELECT
    *
from
    addressinfo
WHERE
    address_id = 'add101'
SELECT
    *
FROM
    memberinfo;

-- 5. Write a stored procedure to insert a blood test record into the bloodtest table.
CREATE PROCEDURE insert_blood_test(
    in blood_id varchar(15),
    in date varchar(25),
    in bloodpressure varchar(15),
    in fbs varchar(15),
    in thal varchar(20),
    in serumcholesterol varchar(20),
    in cardiodiagnosis_cardio_id varchar(20)
) BEGIN
INSERT INTO
    bloodtest(
        blood_id,
        date,
        bloodpressure,
        fbs,
        thal,
        serumcholesterol,
        cardiodiagnosis_cardio_id
    )
VALUES
    (
        blood_id,
        date,
        bloodpressure,
        fbs,
        thal,
        serumcholesterol,
        cardiodiagnosis_cardio_id
    );

END call insert_blood_test(
    'bl100',
    '2020-02-25 00:00:00',
    '156',
    '1',
    '2',
    '268',
    'cid211'
)
SELECT
    *
from
    bloodtest
where
    blood_id = 'bl100';

-- 8. Write a stored procedure to insert an X-ray record into the xray table.
CREATE PROCEDURE insert_xray_record(
    in xray_id varchar(20),
    in date varchar(25),
    in ca int,
    in cardiodiagnosis_cardio_id varchar(20)
) BEGIN
INSERT INTO
    xray(xray_id, date, ca, cardiodiagnosis_cardio_id)
VALUES
    (xray_id, date, ca, cardiodiagnosis_cardio_id);

END drop PROCEDURE insert_xray_record call insert_xray_record('xid221', '2020-02-25 00:00:00', '2', 'cid221')
SELECT
    *
from
    xray
where
    xray_id = 'xid221';

-- 9. Create a stored procedure to insert symptom data into the symptom table.
CREATE PROCEDURE insert_symptom(
    in symptom_id varchar(20),
    in date varchar(25),
    in exang int,
    in oldpeak varchar(20),
    in cp int,
    in cardiodiagnosis_cardio_id varchar(20)
) BEGIN
INSERT INTO
    symptom(
        symptom_id,
        date,
        exang,
        oldpeak,
        cp,
        cardiodiagnosis_cardio_id
    )
VALUES
    (
        symptom_id,
        date,
        exang,
        oldpeak,
        cp,
        cardiodiagnosis_cardio_id
    );

END drop PROCEDURE insert_xray_record call insert_symptom(
    'symid101',
    '2020-02-02 00:00:00',
    '1',
    '0.2',
    '1',
    'cid221'
)
SELECT
    *
from
    symptom
where
    symptom_id = 'symid101';

-- 11. Write a stored procedure with a parameter to get a member by their member_id.
CREATE PROCEDURE GetMemberBy_id(IN p_member_id varchar(45)) BEGIN
SELECT
    *
FROM
    memberinfo
WHERE
    member_id = p_member_id;

END drop PROCEDURE GetMemberById call GetMemberBy_id('M177');

-- 13. Develop a stored procedure to get all diagnoses for a specific member using member_id.
CREATE PROCEDURE get_diagnosis_by_id(in p_member_id varchar(45)) begin
SELECT
    *
from
    cardiodiagnosis
WHERE
    memberinfo_member_id = p_member_id;

end call get_diagnosis_by_id('M177');

-- 14. Write a stored procedure to retrieve blood test records by cardio_id.
CREATE PROCEDURE get_bloodtest_by_id(in p_cardio_id varchar(45)) begin
SELECT
    *
from
    bloodtest
WHERE
    cardiodiagnosis_cardio_id = p_cardio_id;

end call get_bloodtest_by_id('cid221');

SELECT
    *
from
    bloodtest