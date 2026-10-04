SELECT Severity, COUNT(*) AS alerts
FROM transactions WHERE Alert=1 GROUP BY Severity ORDER BY alerts DESC;

SELECT "Account ID", COUNT(*) AS alerts, SUM("Amount EUR") AS alert_value,
       MAX("Risk Score") AS max_score
FROM transactions WHERE Alert=1
GROUP BY "Account ID" ORDER BY max_score DESC, alerts DESC LIMIT 20;

SELECT Country, COUNT(*) AS alerts, SUM("Amount EUR") AS value
FROM transactions WHERE Alert=1 GROUP BY Country ORDER BY alerts DESC;
