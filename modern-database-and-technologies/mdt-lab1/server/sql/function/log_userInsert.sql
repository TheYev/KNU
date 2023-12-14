CREATE TABLE user_log (
  event_id serial PRIMARY KEY,
  event_description TEXT,
  event_timestamp TIMESTAMPTZ
);

CREATE OR REPLACE FUNCTION log_user_insert() RETURNS TRIGGER AS $$
BEGIN
  INSERT INTO user_log (event_description, event_timestamp)
  VALUES ('New user inserted with Id: ' || NEW."Id", NOW());
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;