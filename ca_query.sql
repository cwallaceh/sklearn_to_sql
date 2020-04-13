DROP TABLE IF EXISTS TMP_1;
CREATE TABLE TMP_1 AS
SELECT DF.*,
  `Pclass` * -1.1519 +
  `Age` * -0.0445 +
  `SibSp` * -0.2922 +
  `Parch` * 0.2478 +
  `Fare` * 0.0033 +
  3.3969 AS `linear`
FROM DF;

DROP TABLE IF EXISTS TMP_2;
CREATE TABLE TMP_2 AS
SELECT TMP_1.*,
  1 / (1 + exp(-1 * `linear`)) AS `probability`
FROM TMP_1;
