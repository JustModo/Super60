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
    COUNT(*) AS 'Blood Tests Done'
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
    COUNT(*) AS 'Total Members'
FROM
    memberinfo;

-- To get the total number of blood tests done
SELECT
    COUNT(*) AS 'Total Blood Tests'
FROM
    bloodtest;

-- To get the average cholestrol level for members



-- To get the max peak value in symptoms
-- Get the list of tests done between 2015 Jan 1st and 2019 Jan 31st