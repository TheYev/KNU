CREATE OR REPLACE FUNCTION get_subject_score(subject_id INT) RETURNS INT AS $$
DECLARE 
  subject_score INT;
BEGIN
  SELECT score INTO subject_score FROM "Subject" WHERE "Id" = subject_id;
  RETURN subject_score;
END;
$$ LANGUAGE plpgsql;

SELECT get_subject_score(1);