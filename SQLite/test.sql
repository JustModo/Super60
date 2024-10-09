-- -- Get all members from DB
SELECT * FROM addressinfo
-- -- Where age > 40
WHERE state='Second District';

-- -- Get all members from DB
SElect * FROM memberinfo 
-- -- Where age > 40
WHERE age > 40;

-- Get all members from DB
SElect firstname,lastname,gender FROM memberinfo 
-- Where age > 40
WHERE age > 40;

-- List of patients who are F age between 40-60
SElect * FROM memberinfo 
WHERE gender = 1 AND age BETWEEN 40 AND 60;

-- Aggregate Function
-- Total count
SELECT COUNT(*) FROM memberinfo;

-- Total count of females
SELECT COUNT(*) 'Count of Female' FROM memberinfo 
-- Where female
WHERE gender = 0;

-- Total count of males and females
SELECT 
CASE 
    WHEN gender = 0 THEN 'Male'
    WHEN gender = 1 THEN 'Female'
END AS 'Gender', COUNT(gender) AS 'Count'
FROM memberinfo
GROUP BY gender;
-- Where female

-- Total count of males and females between 40-80
SELECT 
  gender AS 'Gender', 
  COUNT(*) AS 'Count'
FROM memberinfo
WHERE age BETWEEN 40 AND 80
AND gender = '0'
GROUP BY gender;

-- List of diagnosis for the year 2019 June
SELECT * FROM cardiodiagnosis WHERE YEAR(date) = 2019 AND MONTH(date) = 6;

-- Count of diagnosis for the year 2019 June
SELECT COUNT(*) FROM cardiodiagnosis WHERE YEAR(date) = 2019 AND MONTH(date) = 6;

-- Count of diagnosis for the year 2019 June
SELECT * FROM memberinfo ORDER BY username ASC;

-- Merger username with city (old)
SELECT m.username, m.gender, m.age, a.city 
FROM memberinfo m, addressinfo a
WHERE m.member_id = a.memberinfo_member_id;

-- Merger username with city (new)
SELECT m.username, m.gender, m.age, a.city 
FROM memberinfo m INNER JOIN addressinfo a
ON m.member_id = a.memberinfo_member_id;

-- List of people and state name age 60-80

SELECT memberinfo.username, addressinfo.state 
FROM memberinfo INNER JOIN addressinfo
ON memberinfo.member_id = addressinfo.memberinfo_member_id
WHERE memberinfo.age BETWEEN 60 AND 80;

-- total of people in each state order by state aged < 40

SELECT COUNT(*) AS 'Number of Patients', a.state AS 'State'
FROM memberinfo m INNER JOIN addressinfo a
ON m.member_id = a.memberinfo_member_id
WHERE age < 40
GROUP BY a.state
ORDER BY a.state ASC;

-- total of people in each state order by state aged < 40

SELECT COUNT(*) AS 'Number_of_Patients', a.state AS 'State'
FROM memberinfo m INNER JOIN addressinfo a
ON m.member_id = a.memberinfo_member_id
WHERE m.age < 40
GROUP BY a.state
ORDER BY a.state ASC;

-- Total number of ppl diagnosed with heart atk age <40

SELECT COUNT(*) AS 'Number_of_Patients'
FROM memberinfo m INNER JOIN cardiodiagnosis c
ON m.member_id = c.memberinfo_member_id
WHERE m.age < 40 AND c.cardioarrestdetected = 1;

-- List patient name gender age city and diagnosed and their fbs

SELECT 
m.username 'Name', 
m.age 'Age',
m.gender 'Gender',
a.city 'City',
b.fbs 'FBS',
c.cardioarrestdetected 'CA Detected'
FROM memberinfo m 
	INNER JOIn addressinfo a ON m.member_id = a.memberinfo_member_id
	INNER JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
	INNER JOIN bloodtest b ON c.cardio_id = b.cardiodiagnosis_cardio_id
ORDER BY m.username;

-- List number of patients name age city gender diagnosed with HA, rest ECG for the people who been diagnosed with HA for month may 2019

SELECT 
m.username 'Name', 
m.age 'Age',
m.gender 'Gender',
a.city 'City',
e.restecg 'Rest ECG',
c.cardioarrestdetected 'CA Detected'
FROM memberinfo m 
	INNER JOIn addressinfo a ON m.member_id = a.memberinfo_member_id
	INNER JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
    INNER JOIN diseasedetail d ON c.cardio_id = d.cardiodiagnosis_cardio_id
	INNER JOIN ecgreport e ON e.cardiodiagnosis_cardio_id = c.cardio_id
WHERE MONTH(d.diagnoseddate) = 5 AND YEAR(d.diagnoseddate) = 2019
ORDER BY m.username;