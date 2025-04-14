CREATE PROCEDURE risk_factor(IN date1 DATE, IN date2 DATE) BEGIN
SELECT
    m.member_id,
    b.bloodpressure,
    b.fbs,
    b.serumcholesterol,
    w.thalach,
    w.slope,
    c.date,
    calculate_risk_factor(
        b.bloodpressure,
        b.fbs,
        b.serumcholesterol,
        w.thalach,
        w.slope
    ) AS risk_factor
from
    memberinfo m
    INNER JOIN cardiodiagnosis c on c.memberinfo_member_id = m.member_id
    INNER JOIN diseasedetail d ON d.cardiodiagnosis_cardio_id = c.cardio_id
    INNER JOIN bloodtest b ON b.cardiodiagnosis_cardio_id = c.cardio_id
    INNER JOIN wearabledevicedata w ON c.cardio_id = w.cardiodiagnosis_cardio_id
WHERE
    calculate_risk_factor(
        b.bloodpressure,
        b.fbs,
        b.serumcholesterol,
        w.thalach,
        w.slope
    ) > 50
    AND c.date BETWEEN date1
    AND date2;
END;

CALL risk_factor('2019-01-01', '2019-12-31');

CREATE FUNCTION calculate_risk_factor(bp INT, fbs int, chol int, hr int, slope int) RETURNS FLOAT BEGIN DECLARE risk_factor INT;

SET
    risk_factor = (bp * 0.3) +(fbs * 0.25) +(chol * 0.2) +(hr * 0.15) -(slope * 0.1);

RETURN risk_factor;

END;