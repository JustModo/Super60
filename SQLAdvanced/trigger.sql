-- 10
CREATE TRIGGER prevent_invalid_recovery_date BEFORE
UPDATE
    ON diseasedetail FOR EACH ROW BEGIN IF NEW.recovereddate < NEW.diagnoseddate THEN SIGNAL SQLSTATE '45000'
SET
    MESSAGE_TEXT = 'Recovery date cannot be earlier than the diagnosed date';

END IF;

END;

-- 11
CREATE TABLE memberinfo_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    member_id VARCHAR(255),
    old_username VARCHAR(255),
    new_username VARCHAR(255),
    old_firstname VARCHAR(255),
    new_firstname VARCHAR(255),
    old_lastname VARCHAR(255),
    new_lastname VARCHAR(255),
    old_email VARCHAR(255),
    new_email VARCHAR(255),
    old_gender VARCHAR(255),
    new_gender VARCHAR(255),
    old_age INT,
    new_age INT,
    old_phonenumber BIGINT,
    new_phonenumber BIGINT,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TRIGGER log_memberinfo_updates
AFTER
UPDATE
    ON memberinfo FOR EACH ROW BEGIN
INSERT INTO
    memberinfo_log (
        member_id,
        old_username,
        new_username,
        old_firstname,
        new_firstname,
        old_lastname,
        new_lastname,
        old_email,
        new_email,
        old_gender,
        new_gender,
        old_age,
        new_age,
        old_phonenumber,
        new_phonenumber,
        updated_at
    )
VALUES
    (
        OLD.member_id,
        OLD.username,
        NEW.username,
        OLD.firstname,
        NEW.firstname,
        OLD.lastname,
        NEW.lastname,
        OLD.email,
        NEW.email,
        OLD.gender,
        NEW.gender,
        OLD.age,
        NEW.age,
        OLD.phonenumber,
        NEW.phonenumber,
        NOW()
    );

END;

SELECT
    *
FROM
    log -- 12
    CREATE TRIGGER prevent_high_bp BEFORE
INSERT
    ON bloodtest FOR EACH ROW BEGIN IF NEW.bloodpressure > 180 THEN SIGNAL SQLSTATE '45000'
SET
    MESSAGE_TEXT = 'Blood pressure exceeds critical level';

END IF;

END;

--4
CREATE TRIGGER capitalize_city_name BEFORE
INSERT
    ON addressinfo FOR EACH ROW BEGIN
SET
    NEW.city = CONCAT(
        UPPER(LEFT(NEW.city, 1)),
        LOWER(SUBSTRING(NEW.city, 2))
    );

END;

-- 13
CREATE TRIGGER update_disease_status BEFORE
UPDATE
    ON diseasedetail FOR EACH ROW BEGIN IF NEW.recovereddate IS NOT NULL
    AND NEW.recovereddate <= CURDATE() THEN
SET
    NEW.status = 'Recovered';

END IF;

END;

-- 14
CREATE TRIGGER check_member_exists_cardio BEFORE
INSERT
    ON cardiodiagnosis FOR EACH ROW BEGIN DECLARE member_exists INT;

SELECT
    COUNT(*) INTO member_exists
FROM
    memberinfo
WHERE
    member_id = NEW.memberinfo_member_id;

IF member_exists = 0 THEN SIGNAL SQLSTATE '45000'
SET
    MESSAGE_TEXT = "Member doesnt exists";

END IF;

END;

-- Vidyaa
-- 1 Write a trigger to update the recovereddate when a disease record is updated.
CREATE TABLE disease_records (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_name VARCHAR(100),
    status VARCHAR(50),
    recovereddate DATETIME DEFAULT NULL
);

CREATE TRIGGER update_recovered_date BEFORE
UPDATE
    ON disease_records FOR EACH ROW BEGIN IF NEW.status = 'Recovered'
    AND OLD.status != 'Recovered' THEN
SET
    NEW.recovereddate = NOW();

END IF;

END;

INSERT INTO
    disease_records (patient_name, status)
VALUES
    ('John Doe', 'Sick');

UPDATE
    disease_records
SET
    status = 'Recovered'
WHERE
    patient_name = 'John Doe';

SELECT
    *
FROM
    disease_records;

-- SHUBHAA
-- 9
CREATE TRIGGER before_insert_bloodtest BEFORE
INSERT
    ON bloodtest FOR EACH ROW BEGIN IF NEW.thal IS NULL THEN
SET
    NEW.thal = 2;

END IF;

END;

INSERT INTO
    cardiodiagnosis (
        cardio_id,
        cardioarrestdetected,
        date,
        memberinfo_member_id
    )
VALUES
    ('C122', 1, '2025-03-07 12:00:00', 'M1');

-- 8
CREATE TRIGGER before_insert_update_memberinfo BEFORE
INSERT
    ON memberinfo FOR EACH ROW BEGIN IF NEW.age <= 0 THEN SIGNAL SQLSTATE '45000'
SET
    MESSAGE_TEXT = 'Error: Age must be a positive number greater than zero.';

END IF;

END;

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
        'M006',
        'john_doe',
        'John',
        'Doe',
        -5,
        'Male',
        'john@example.com',
        9876543210
    );

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
        'M007',
        'jane_doe',
        'Jane',
        'Doe',
        25,
        'Female',
        'jane@example.com',
        9876543211
    );