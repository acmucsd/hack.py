DROP TABLE IF EXISTS todoitem;

CREATE TABLE todoitem (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  todotype TEXT NOT NULL,
  todotext TEXT NOT NULL
);