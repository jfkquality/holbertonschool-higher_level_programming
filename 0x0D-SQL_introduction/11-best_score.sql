-- ists all records with score >= 10 of the table second_table of hbtn_0c_0.
-- Results should display both the score and the name (in this order)
-- Records should be ordered by score (top first)
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC
