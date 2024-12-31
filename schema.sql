CREATE TABLE bookmark (amharic TEXT, english TEXT, date DATETIME DEFAULT (CURRENT_TIMESTAMP));
CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE history (amharic TEXT NOT NULL, english TEXT, date DATETIME DEFAULT (CURRENT_TIMESTAMP));
CREATE TABLE dictionary (id INTEGER PRIMARY KEY AUTOINCREMENT, amharic VARCHAR (25), english TEXT, wordtype VARCHAR (10), reference VARCHAR (25));
