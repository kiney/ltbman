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

--- ltb bewegen ---
UPDATE ltbs
SET location = 1
WHERE ltbid = 132
