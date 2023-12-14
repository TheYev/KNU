CREATE OR REPLACE FUNCTION get_faculty_and_groups()
RETURNS TABLE (
  FacultyId INT,
  FacultyName TEXT,
  GroupId INT,
  GroupName TEXT,
  GroupCreateAt TIMESTAMP(3) WITHOUT TIME ZONE
) AS $$
BEGIN
  RETURN QUERY
  SELECT F."Id" AS FacultyId, F."Name" AS FacultyName, GC."Id" AS GroupId, GC."Name" AS GroupName, GC."GroupCreateAt"
  FROM "Faculty" F
  LEFT JOIN "GroopCollection" GC ON F."Id" = GC."FacultyId";
END;
$$ LANGUAGE plpgsql;

SELECT * FROM get_faculty_and_groups();