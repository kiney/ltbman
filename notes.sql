-- alle vorhandenen ltbs
SELECT ltbs.ltbid, ltbs.title, locations.name AS location
FROM ltbs
INNER JOIN locations ON ltbs.location = locations.id
WHERE ltbs.present = 1;

--- fehlende ltbs
SELECT ltbs.ltbid, ltbs.title
FROM ltbs
WHERE ltbs.present = 0;

--- verschoellene ltbs
SELECT ltbs.ltbid, ltbs.title, locations.name AS location
FROM ltbs
INNER JOIN locations ON ltbs.location = locations.id
WHERE
  ltbs.present = 1 AND
  locations.id = 0;

--- ltbs nach ort
SELECT count(ltbs.ltbid), locations.name AS location
FROM ltbs
INNER JOIN locations ON ltbs.location = locations.id
WHERE ltbs.present = 1
GROUP BY locations.id;

--- ltbs in z.B. hannover
SELECT ltbs.ltbid, ltbs.title
FROM ltbs
INNER JOIN locations ON ltbs.location = locations.id
WHERE locations.id = 1;

--- ltb bewegen
UPDATE ltbs
SET location = 1
WHERE ltbid = 132

--- locations table mit subquerys um namen ergänzen
SELECT ltbid,
(SELECT name FROM locations WHERE locations.id = moves.OldLocation) AS old,
(SELECT name FROM locations WHERE locations.id = moves.NewLocation) AS new,
Time
FROM moves;
--- JOIN basiert version, äquivalent?
SELECT m.ltbid, l1.name AS old, l2.name AS new, m.Time
FROM moves m
JOIN locations l1 ON m.OldLocation = l1.id
JOIN locations l2 ON m.NewLocation = l2.id
