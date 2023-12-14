CREATE TRIGGER group_changes_trigger
AFTER INSERT OR UPDATE OR DELETE ON "GroopCollection"
FOR EACH ROW
EXECUTE FUNCTION log_groop_collection_changes();


UPDATE "GroopCollection" SET "Name" = 'wwsssfgt' WHERE "Id" = 1;