-- creates second_table in  hbtn_0c_0 and add multiples rows.
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);

INSERT INTO second_table (id, name, score)
VALUES
	(5, "Joe", 5),
	(6, "Pam", 3),
	(7, "Lauren", 4),
	(12, "Alexis", 5);
