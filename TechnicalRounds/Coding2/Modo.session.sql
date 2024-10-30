-- Retrieve the first name, last name, and date of birth of all members who were born after "1990-01-01".
-- SELECT
--     m.firstname,
--     m.lastname,
--     m.age
-- FROM
--     memberinfo m
-- WHERE
--     m.age > 28
-- Find the member IDs and addresses of all members living in the state "California".
-- SELECT
--     m.member_id,
--     a.country,
--     a.city,
--     a.state
-- FROM
--     memberinfo m
--     INNER JOIN addressinfo a ON a.memberinfo_member_id = m.member_id
-- WHERE a.state = 'California'
-- Calculate the total number of unique symptoms recorded in each month over the last year.
-- SELECT
--     MONTH(s.date),
--     COUNT(*)
-- FROM
--     memberinfo m
--     INNER JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
--     INNER JOIN symptom s ON c.cardio_id = s.cardiodiagnosis_cardio_id
-- GROUP BY
--     MONTH(s.date)
-- Retrieve the average cholesterol levels for members aged over 50, grouped by gender
-- SELECT
--     m.gender,
--     AVG(b.serumcholesterol)
-- FROM
--     memberinfo m
--     INNER JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
--     INNER JOIN bloodtest b ON c.cardio_id = b.cardiodiagnosis_cardio_id
-- WHERE
--     m.age > 50
-- GROUP BY
--     m.gender
-- Calculate the total number of ECG tests, blood tests, and cholesterol tests conducted each month for the last 6 months.
-- SELECT
--     MONTH(b.date),
--     COUNT(b.serumcholesterol) as "Cholesterol tests",
--     COUNT(e.ecg_id) as "ECG tests",
--     COUNT(b.blood_id) as "Blood tests"
-- FROM
--     memberinfo m
--     INNER JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
--     INNER JOIN ecgreport e ON c.cardio_id = e.cardiodiagnosis_cardio_id
--     INNER JOIN bloodtest b ON c.cardio_id = b.cardiodiagnosis_cardio_id
-- WHERE
--     MONTH(b.date) BETWEEN 1
--     AND 6
-- GROUP BY
--     MONTH(b.date)
-- List the top 5 members who reported the highest number of symptoms along with their most frequent symptom in the past year.
-- SELECT
--     m.firstname,
--     COUNT(s.symptom_id)
-- FROM
--     memberinfo m
--     INNER JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
--     INNER JOIN symptom s ON c.cardio_id = s.cardiodiagnosis_cardio_id
-- GROUP BY
--     m.firstname
-- ORDER BY
--     COUNT(s.symptom_id) DESC
-- LIMIT
--     5
-- SELECT
--     a.state,
--     COUNT(DISTINCT m.member_id) AS member_count
-- FROM
--     addressinfo a
--     JOIN memberinfo m ON a.member_id = m.member_id
--     JOIN symptom s ON m.member_id = s.member_id
--     JOIN ecgreport ecg ON m.member_id = ecg.member_id
-- WHERE
--     s.symptomdescription = 'Shortness of Breath'
--     AND ecg.result != 'Normal'
-- GROUP BY
--     a.state
-- ORDER BY
--     member_count DESC
-- LIMIT
--     3;
SELECT
    m.member_id,
    AVG(wd.heart_rate) AS avg_heart_rate,
    MAX(wd.heart_rate) AS max_heart_rate
FROM
    memberinfo m
    JOIN wearabledevicedata wd ON m.member_id = wd.member_id
    JOIN symptom s ON m.member_id = s.member_id
    JOIN ecgreport ecg ON m.member_id = ecg.member_id
WHERE
    s.symptomdescription = 'Dizziness'
    AND s.reportdate >= DATEADD(MONTH, -3, GETDATE())
GROUP BY
    m.member_id;