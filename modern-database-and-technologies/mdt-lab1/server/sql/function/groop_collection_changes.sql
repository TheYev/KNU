CREATE OR REPLACE FUNCTION groop_collection_changes()
RETURNS TRIGGER AS $$
BEGIN
  IF TG_OP = 'INSERT' THEN
    RAISE NOTICE 'New group inserted with Id: %', NEW."Id";
  ELSIF TG_OP = 'UPDATE' THEN
    RAISE NOTICE 'Group with Id: % updated', NEW."Id";
  ELSIF TG_OP = 'DELETE' THEN
    RAISE NOTICE 'Group with Id: % deleted', OLD."Id";
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;