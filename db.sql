BEGIN TRANSACTION;
CREATE TABLE `moves` (
	`MoveId`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`OldLocation`	INTEGER NOT NULL,
	`NewLocation`	INTEGER NOT NULL
);
CREATE TABLE "ltbs" (
	`ltbid`	INTEGER NOT NULL UNIQUE,
	`title`	TEXT,
	`present`	INTEGER NOT NULL,
	`location`	INTEGER NOT NULL,
	`dupes`	INTEGER DEFAULT 0,
	PRIMARY KEY(ltbid)
);
CREATE TABLE "locations" (
	`id`	INTEGER NOT NULL UNIQUE,
	`name`	TEXT NOT NULL,
	PRIMARY KEY(id)
);
INSERT INTO `locations` (id,name) VALUES (0,'unknown'),
 (1,'Hannover'),
 (2,'Marburg'),
 (3,'Harz');
COMMIT;
