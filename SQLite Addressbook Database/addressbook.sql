DROP TABLE IF EXISTS contacts;

CREATE TABLE contacts (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	first	TEXT NOT NULL,
	last	TEXT NOT NULL,
	phone	TEXT NOT NULL
);
