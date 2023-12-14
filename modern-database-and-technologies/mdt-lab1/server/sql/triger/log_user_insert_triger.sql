CREATE TRIGGER user_insert_trigger
AFTER INSERT
ON "User"
FOR EACH ROW
EXECUTE FUNCTION log_user_insert();

INSERT INTO "User" ("Email", "Password", "FirstName", "LastName", "CountryId")
VALUES ('example@example.com', 'password123', 'John', 'Doe', 1);
SELECT * FROM user_log;