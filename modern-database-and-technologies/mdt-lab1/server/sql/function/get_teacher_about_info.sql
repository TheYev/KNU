CREATE OR REPLACE FUNCTION get_teacher_about_info(teacher_id INT)
RETURNS TABLE (
  LastName TEXT,
  Age INT,
  YearEndUniversity INT,
  YearStartWork INT,
  Phone INT,
  Email TEXT,
  Telegram TEXT
) AS $$
BEGIN
  RETURN QUERY
  SELECT HT."LastName", HA."Age", HA."YearEndUniversity", HA."YearStartWork", HA."Phone", HA."Email", HA."Telegram"
  FROM "HeadTecher" HT
  INNER JOIN "HeadTecherAbout" HA ON HT."Id" = HA."HeadTecherId"
  WHERE HT."Id" = teacher_id;
END;
$$ LANGUAGE plpgsql;

SELECT * FROM get_teacher_about_info_with_lastname(1);

