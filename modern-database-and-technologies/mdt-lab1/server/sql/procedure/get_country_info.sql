CREATE OR REPLACE PROCEDURE get_country_info(country_id INT)
LANGUAGE plpgsql
AS $$
DECLARE
  country_name TEXT;
  president_name TEXT;
BEGIN
  SELECT "Name", "PresidentName"
  INTO country_name, president_name
  FROM "Country"
  WHERE "Id" = country_id;

  RAISE NOTICE 'Country Name: %', country_name;
  RAISE NOTICE 'President: %', president_name;
END;
$$;

CALL get_country_info(1);