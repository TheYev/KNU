CREATE OR REPLACE PROCEDURE get_user_info(user_id INT) AS $$
DECLARE
  user_record "User"%ROWTYPE;
BEGIN
  SELECT * INTO user_record FROM "User" WHERE "Id" = user_id;
  
  RAISE NOTICE 'User Id: %, Email: %, FirstName: %, LastName: %', user_record."Id", user_record."Email", user_record."FirstName", user_record."LastName";
END;
$$ LANGUAGE plpgsql;

CALL get_user_info(1);