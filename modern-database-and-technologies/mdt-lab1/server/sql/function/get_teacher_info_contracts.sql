CREATE OR REPLACE FUNCTION get_teacher_info_contracts(teacher_id INT)
RETURNS TABLE (
  Last_Name TEXT,
  ContractId INT,
  Status BOOLEAN,
  TeacherJoinToContact TIMESTAMP(3) WITHOUT TIME ZONE,
  TeacherExittContact TIMESTAMP(3) WITHOUT TIME ZONE
) AS $$
BEGIN
  RETURN QUERY
  SELECT HT."LastName", TC."Id", TC."status", TC."TeacherJoinToContact", TC."TeacherExittContact"
  FROM "HeadTecher" HT
  LEFT JOIN "TeacherContractCollection" TC ON HT."Id" = TC."TeacherId"
  WHERE HT."Id" = teacher_id;
END;
$$ LANGUAGE plpgsql;

SELECT * FROM get_teacher_info_with_contracts(1);