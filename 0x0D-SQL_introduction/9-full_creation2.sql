-- creates second_table in  hbtn_0c_0 and add multiples rows.
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);

INSERT INTO second_table (id, name, score)
VALUES
	(5, "Jim", 10),
	(6, "Alex", 3),
	(7, "Bob", 14),
	(8, "Jim", 10),
	(9, "", 3),
	(10, "Sam", 14),
	(11, "", 8),
	(12, "Mary", 8);
