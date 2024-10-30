-- SELECT
--     m.member_id,
--     COUNT(b.test_id) AS blood_tests,
--     COUNT(ecg.report_id) AS ecg_tests
-- FROM
--     memberinfo m
--     LEFT JOIN bloodtest b ON m.member_id = b.member_id
--     LEFT JOIN ecgreport ecg ON m.member_id = ecg.member_id
-- WHERE
--     EXISTS (
--         SELECT
--             1
--         FROM
--             cardiodiagnosis c
--         WHERE
--             c.member_id = m.member_id
--             AND c.diagnosis = 'Hypertension'
--     )
-- GROUP BY
--     m.member_id;
SELECT
    (m.age / 10) * 10 AS age_group,
    AVG(b.systolic) AS avg_systolic,
    AVG(b.diastolic) AS avg_diastolic
FROM
    memberinfo m
    JOIN bloodtest b ON m.member_id = b.member_id
WHERE
    b.testdate >= DATEADD(YEAR, -1, GETDATE())
GROUP BY
    (m.age / 10) * 10;