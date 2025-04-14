CREATE PROCEDURE get_info_by_id(IN member_id_p VARCHAR(15)) BEGIN
SELECT
    firstname,
    lastname,
    age
FROM
    memberinfo
WHERE
    member_id = member_id_p;

END CALL get_info_by_id("M100");

DROP PROCEDURE get_info_by_id;

-- Gender Count
CREATE PROCEDURE get_gender_count() BEGIN
SELECT
    CASE
        WHEN gender = '0' THEN 'Female'
        WHEN gender = '1' THEN 'Male'
    END AS 'Gender',
    COUNT(*)
FROM
    memberinfo
GROUP BY
    gender;

END;

CALL get_gender_count();

-- Function Calls
CREATE FUNCTION get_member_function(gender INT) RETURNS VARCHAR(45) BEGIN DECLARE result VARCHAR(45);

IF gender = 0 THEN
SET
    result = 'female';

ELSE
SET
    result = 'male';

END IF;

RETURN result;

END;

DROP FUNCTION get_member_function;

SELECT
    get_member_function(1);

-- Write a store procedure which will accept username, firstname, last name, age, gender, email and phone number Username should be unique
-- Write a function convert charcter male female to 0 and 1 and store
-- Username name should be unique, if the username is already present in the memberinfo table, raise an exception. "Username is already Bound"
-- Take the maximum of the member iD and append 1 to that and insert the new member id as the primary key
-- Look into triggers

CREATE FUNCTION gender_to_numstring(gender varchar(15)) RETURNS varchar(15)
BEGIN
    DECLARE result varchar(15);
    IF gender = "male" THEN
        SET result = "1";
    ELSE
        SET result = "0";
    END IF;
    RETURN result;
END;

CREATE FUNCTION check_unique(username_p varchar(15)) RETURNS int
BEGIN
    DECLARE result int;
    SELECT COUNT(*) INTO result FROM memberinfo WHERE username = username_p;

    RETURN result;
END;


CREATE FUNCTION next_id() RETURNS VARCHAR(15)
BEGIN
    DECLARE result INT;

    SELECT MAX(CAST(SUBSTRING(member_id, 2) AS UNSIGNED))
    INTO result
    FROM memberinfo;

    RETURN CONCAT('M', result + 1);
END;


CREATE PROCEDURE insert_into_table(
    IN username varchar(15),
    IN firstname varchar(15),
    IN lastname varchar(15),
    IN age int,
    IN gender varchar(15),
    IN email varchar(15),
    IN phonenumber BIGINT
) BEGIN
    DECLARE gender_numstring VARCHAR(15);
    DECLARE new_id VARCHAR(15);
    SET gender_numstring = gender_to_numstring(gender);
    
    IF check_unique(username) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Username is already Bound';
    END IF;

    SET new_id = next_id();

    INSERT INTO memberinfo (member_id, username, firstname, lastname, age, gender, email, phonenumber)
    VALUES (new_id, username, firstname, lastname, age, gender_numstring, email, phonenumber);
        

END;


CALL insert_into_table("hello","Yash","Laxman",20,"male","abc@123",1234567890);

SELECT * FROM memberinfo WHERE username = "hello";
DELETE FROM memberinfo WHERE username = "hello";

SELECT check_unique("hello")