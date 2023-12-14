CREATE OR REPLACE FUNCTION get_user_count() RETURNS INT AS $$
DECLARE 
  user_count INT;
BEGIN
  SELECT COUNT(*) INTO user_count FROM "User";
  RETURN user_count;
END;
$$ LANGUAGE plpgsql;

SELECT get_user_count();