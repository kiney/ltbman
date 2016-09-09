BEGIN TRANSACTION;
CREATE TABLE `moves` (
	`MoveId`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`OldLocation`	INTEGER NOT NULL,
	`NewLocation`	INTEGER NOT NULL
);
CREATE TABLE "ltbs" (
	`Field1`	INTEGER NOT NULL UNIQUE,
	`title`	TEXT,
	`present`	INTEGER NOT NULL,
	`location`	INTEGER NOT NULL,
	`dupes`	INTEGER DEFAULT 0,
	PRIMARY KEY(Field1)
);
CREATE TABLE "locations" (
	`id`	INTEGER NOT NULL UNIQUE,
	`name`	TEXT NOT NULL,
	PRIMARY KEY(id)
);
INSERT INTO `locations` VALUES (0,'unbekannt');
INSERT INTO `locations` VALUES (1,'Hannover');
INSERT INTO `locations` VALUES (2,'Marburg');
INSERT INTO `locations` VALUES (3,'Harz');
COMMIT;
