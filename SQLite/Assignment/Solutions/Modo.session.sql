-- Get all the predictions 
SELECT
    *
FROM
    cardiodiagnosis c;

-- Get all the predictions for the day
SELECT
    *
FROM
    cardiodiagnosis c
    INNER JOIN diseasedetail d ON c.cardio_id = d.cardiodiagnosis_cardio_id
WHERE
    d.diagnoseddate = '2019-01-25';

-- Get all the predictions for the day and sort it based on highest percentage of probability at the top
-- ??
-- Get all the unique cities 
SELECT
    UNIQUE(a.city)
FROM
    addressinfo a
ORDER BY
    a.city ASC;

-- Get all the members who are from a city  'Burgos'
SELECT
    *
FROM
    memberinfo m
    INNER JOIN addressinfo a ON a.memberinfo_member_id = m.member_id
WHERE
    a.city = 'Burgos';

-- Get all the members who are from 'flora' city
SELECT
    *
FROM
    memberinfo m
    INNER JOIN addressinfo a ON a.memberinfo_member_id = m.member_id
WHERE
    a.city = 'Flora';

-- Get the total number of bloodtests done for Aisha
SELECT
    m.firstname AS 'Name',
    COUNT(*) AS 'BloodTestsDone'
FROM
    memberinfo m
    INNER JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
    INNER JOIN bloodtest b ON b.cardiodiagnosis_cardio_id = c.cardio_id
WHERE
    m.firstname = 'Aisha';

-- Get the xray details of Ajay whose cardio was done on 26th of Jan 2019
SELECT
    m.firstname,
    x.ca,
    x.date,
    x.xray_id
FROM
    memberinfo m
    INNER JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
    INNER JOIN xray x ON x.cardiodiagnosis_cardio_id = c.cardio_id
WHERE
    m.firstname = 'Ajay'
    AND c.date = '2019-01-26';

-- Get all the members who are from city burgos and flora
SELECT
    m.firstname,
    a.city
FROM
    memberinfo m
    INNER JOIN addressinfo a ON m.member_id = a.memberinfo_member_id
WHERE
    a.city = 'burgos'
    OR a.city = 'flora';

-- Get the total number of bloodtests done for aberson
SELECT
    COUNT(*)
FROM
    memberinfo m
    INNER JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
    INNER JOIN bloodtest b ON b.cardiodiagnosis_cardio_id = c.cardio_id
WHERE
    m.lastname = 'aberson';

-- Get all address details for member ID M303
SELECT
    a.address_id,
    a.city,
    a.country,
    a.pincode,
    a.state
FROM
    memberinfo m
    INNER JOIN addressinfo a ON m.member_id = a.memberinfo_member_id
WHERE
    m.member_id = 'M303';

-- Get all xray details for cardio id cid 122
SELECT
    *
FROM
    cardiodiagnosis c
    INNER JOIN xray x on c.cardio_id = x.cardiodiagnosis_cardio_id
WHERE
    cardio_id = 'cid122';

-- Get all symptom details whose cardio ID = CID250 and CID300
SELECT
    *
FROM
    cardiodiagnosis c
    INNER JOIN symptom s ON c.cardio_id = s.cardiodiagnosis_cardio_id
WHERE
    c.cardio_id = 'cid250'
    OR c.cardio_id = 'cid300';

-- Get all symptom details for month july and year 2019
SELECT
    *
FROM
    symptom
WHERE
    MONTH(date) = '7'
    AND YEAR(date) = '2019';

-- Get xray details for member with lastname "dailley"
SELECT
    *
FROM
    memberinfo m
    INNER JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
    INNER JOIN xray x ON x.cardiodiagnosis_cardio_id = c.cardio_id
WHERE
    m.lastname = 'dailley';

-- Get wearabledevicedata details from cardio ID from CID100 to CID200
SELECT
    *
FROM
    wearabledevicedata w
    INNER JOIN cardiodiagnosis c ON c.cardio_id = w.cardiodiagnosis_cardio_id
WHERE
    c.cardio_id = 'cid100'
    OR c.cardio_id = 'cid200';

-- Display all cardiodiagnosis details who first name start from letter "A"
SELECT
    m.firstname,
    c.cardio_id,
    c.cardioarrestdetected,
    c.date
FROM
    memberinfo m
    INNER JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
WHERE
    m.firstname LIKE 'A%';

-- Display all cardiodiagnosis details who first name start from letter "A" and ends at letter "A"
SELECT
    m.firstname,
    c.cardio_id,
    c.cardioarrestdetected,
    c.date
FROM
    memberinfo m
    INNER JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
WHERE
    m.firstname LIKE 'A%'
    AND m.firstname LIKE '%A';

-- To get all the members from the MemberInfo
SELECT
    username
FROM
    memberinfo;

-- To get all the addresess of Members
SELECT
    m.username,
    a.city,
    a.country,
    a.pincode,
    a.state
FROM
    memberinfo m
    INNER JOIN addressinfo a ON m.member_id = a.memberinfo_member_id;

-- To get a list of wearable device information
SELECT
    *
FROM
    wearabledevicedata;

-- To get a list of all the blood tests done
SELECT
    *
FROM
    bloodtest;

-- Get a list of members who are aged greater than 50
SELECT
    *
FROM
    memberinfo
WHERE
    age > 50;

-- To get list of addresses for the city flora
SELECT
    *
FROM
    addressinfo
WHERE
    city = 'flora';

-- Get list of all unique states
SELECT
    UNIQUE(a.state) AS 'States'
FROM
    addressinfo a;

-- Get the total number of members in the database
SELECT
    COUNT(*) AS 'TotalMembers'
FROM
    memberinfo;

-- To get the total number of blood tests done
SELECT
    COUNT(*) AS 'TotalBloodTests'
FROM
    bloodtest;

-- To get the average cholestrol level for members
SELECT
    m.username,
    b.serumcholesterol
FROM
    memberinfo m
    INNER JOIN cardiodiagnosis c ON c.memberinfo_member_id = m.member_id
    INNER JOIN bloodtest b ON b.cardiodiagnosis_cardio_id = c.cardio_id;

-- To get the max peak value in symptoms
SELECT
    MAX(s.oldpeak) as 'MaxPeakValue'
FROM
    memberinfo m
    INNER JOIN cardiodiagnosis c ON c.memberinfo_member_id = m.member_id
    INNER JOIN symptom s ON c.cardio_id = s.cardiodiagnosis_cardio_id;

-- Get the list of tests done between 2015 Jan 1st and 2019 Jan 31st
SELECT
    *
FROM
    bloodtest
WHERE
    date BETWEEN '2019-01-01'
    AND '2019-01-31';

-- Get the number of males and females aged between 50 and 60
SELECT
    CASE
        WHEN gender = 0 THEN 'Female'
        WHEN gender = 1 THEN 'Male'
    END AS 'Gender',
    COUNT(*) AS 'Count'
FROM
    memberinfo
WHERE
    age BETWEEN 50
    AND 60
GROUP BY
    gender;

-- Get the list of tests where blood pressure is between 100 and 200
SELECT
    *
FROM
    bloodtest
WHERE
    bloodpressure BETWEEN 100
    AND 200;

-- Get the list of symptoms diagnosed for patients
SELECT
    *
FROM
    symptom;

-- Get the average age of patients in the database
SELECT
    AVG(age) AS 'AverageAge'
FROM
    memberinfo;

-- Get the total cities for each state available
SELECT
    state AS 'State',
    COUNT(city) AS 'NumberOfCities'
FROM
    addressinfo
GROUP BY
    state;

-- Get number of Patients between age group 
-- 10-20
-- 20-30
-- 30-40
-- 40-50
-- 50-60
-- 60-70
SELECT
    CASE
        WHEN age BETWEEN 10
        AND 20 THEN '10-20'
        WHEN age BETWEEN 20
        AND 30 THEN '20-30'
        WHEN age BETWEEN 30
        AND 40 THEN '30-40'
        WHEN age BETWEEN 40
        AND 50 THEN '40-50'
        WHEN age BETWEEN 50
        AND 60 THEN '50-60'
        WHEN age BETWEEN 60
        AND 70 THEN '60-70'
        ELSE '70+'
    END AS AgeRange,
    COUNT(*) AS `Count`
FROM
    memberinfo
GROUP BY
    AgeRange;

-- Get the list of meembers and their address
SELECT
    *
FROM
    memberinfo m
    INNER JOIN addressinfo a ON m.member_id = a.memberinfo_member_id;

-- Get the list of meembers and their cardiohistory
SELECT
    *
FROM
    memberinfo m
    INNER JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id;

-- Get the list of meembers and their diseases
SELECT
    *
FROM
    memberinfo m
    INNER JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
    INNER JOIN diseasedetail d ON d.cardiodiagnosis_cardio_id = c.cardio_id;

-- To find the list of female who have been digonised with heart attack
SELECT
    *
FROM
    memberinfo m
    INNER JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
WHERE
    m.gender = 0;

-- get the list of female members and their cardio information for people aged above 50
SELECT
    *
FROM
    memberinfo m
    INNER JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
WHERE
    m.gender = 0
    AND age > 50;

-- To get the list of males who have their blood pressure > 140 and not had a heart attack
SELECT
    *
FROM
    memberinfo m
    INNER JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
    INNER JOIN bloodtest b ON b.cardiodiagnosis_cardio_id = c.cardio_id
WHERE
    b.bloodpressure > 140
    AND c.cardioarrestdetected = 0
    and m.gender = 1;

-- To get the list of members who had heart attack from state "mountain province"
SELECT
    *
FROM
    memberinfo m
    INNER JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
    INNER JOIN addressinfo a ON m.member_id = a.memberinfo_member_id
WHERE
    a.state = 'mountain province';

-- To get the list of members who are males and their disease with their symptoms for people aged less than 40
SELECT
    *
FROM
    memberinfo m
    INNER JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
    INNER JOIN diseasedetail d ON d.cardiodiagnosis_cardio_id = c.cardio_id
    INNER JOIN symptom s on s.cardiodiagnosis_cardio_id = c.cardio_id
WHERE
    m.age < 40
    AND m.gender = 1;

-- To get count of members from "mountain province" aged between 50 and 60
SELECT
    COUNT(*) AS 'Count'
FROM
    memberinfo m
    INNER JOIN addressinfo a ON m.member_id = a.memberinfo_member_id
WHERE
    a.state = 'mountain province'
    AND m.age BETWEEN 50
    AND 60;

-- To get the count of male and female members who have blood pressure > 140 and detected heart attack
SELECT
    CASE
        WHEN gender = '0' THEN 'Female'
        WHEN gender = '1' THEN 'Male'
    END AS 'Gender',
    COUNT(*)
FROM
    memberinfo m
    INNER JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
    INNER JOIN bloodtest b ON b.cardiodiagnosis_cardio_id = c.cardio_id
WHERE
    b.bloodpressure > 140
    AND c.cardioarrestdetected = 1
GROUP BY
    gender;

-- Average blood pressure of people aged between 40-50 and 50-60
SELECT
    CASE
        WHEN m.age BETWEEN 40
        AND 50 THEN '40-50'
        WHEN m.age BETWEEN 50
        AND 60 THEN '50-60'
    END AS AgeRange,
    AVG(b.bloodpressure) AS 'Blood Pressure'
FROM
    memberinfo m
    JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
    JOIN bloodtest b ON c.cardio_id = b.cardiodiagnosis_cardio_id
WHERE
    m.age BETWEEN 40
    AND 60
GROUP BY
    AgeRange;

-- To get the list of diseases for people having high blood pressure in the range of 120 - 180 sorted across gender
SELECT
    d.diagnoseddate,
    d.isrecovered,
    d.recovereddate,
    m.gender
FROM
    memberinfo m
    INNER JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
    INNER JOIN diseasedetail d ON c.cardio_id = d.cardiodiagnosis_cardio_id
    INNER JOIN bloodtest b ON b.cardiodiagnosis_cardio_id = c.cardio_id
WHERE
    b.bloodpressure BETWEEN 120
    AND 180
ORDER BY
    m.gender;

-- To get the count of people who have got their xrays every month from the state of Special Province
SELECT
    MONTH(x.date) as month,
    COUNT(*)
FROM
    memberinfo m
    INNER JOIN addressinfo a ON m.member_id = a.memberinfo_member_id
    INNER JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
    INNER JOIN xray x ON x.cardiodiagnosis_cardio_id = c.cardio_id
WHERE
    a.state = 'special provinces'
GROUP BY
    month;

-- To get the average age of people diagnosed with heart attack for each state across male and female
SELECT
    a.state,
    AVG(
        CASE
            WHEN m.gender = '0' THEN m.age
        END
    ) AS 'Female',
    AVG(
        CASE
            WHEN m.gender = '1' THEN m.age
        END
    ) AS 'Male'
FROM
    memberinfo m
    INNER JOIN addressinfo a ON m.member_id = a.memberinfo_member_id
    INNER JOIN cardiodiagnosis c ON c.memberinfo_member_id = m.member_id
GROUP BY
    a.state;

-- To get the count of people for each state having been diagnosed with heart attack who have slope value as 2 and having had atleast 1 xray and 1 symptom

