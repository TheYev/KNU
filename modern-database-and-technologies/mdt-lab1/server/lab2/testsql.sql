-- StudiBook
INSERT INTO public."StudiBook"( "AuthorFullName", "BookName")
	VALUES ('asd1', 'zxc1');

SELECT "Id", "AuthorFullName", "BookName"
	FROM public."StudiBook"
	where "Id" = 1;

UPDATE public."StudiBook"
	SET "AuthorFullName"='updateAuthorName', "BookName"='updateBookName'
	WHERE "Id" = 1;

DELETE FROM public."StudiBook"
	WHERE "Id" = 1;



INSERT INTO public."StudiBook"( "AuthorFullName", "BookName")
	VALUES ('asd1', 'zxc1');
INSERT INTO public."StudiBook"( "AuthorFullName", "BookName")
	VALUES ('asd1', 'zxc1');
INSERT INTO public."StudiBook"( "AuthorFullName", "BookName")
	VALUES ('asd1', 'zxc1');
INSERT INTO public."StudiBook"( "AuthorFullName", "BookName")
	VALUES ('asd1', 'zxc1');
INSERT INTO public."StudiBook"( "AuthorFullName", "BookName")
	VALUES ('asd1', 'zxc1');
INSERT INTO public."StudiBook"( "AuthorFullName", "BookName")
	VALUES ('asd1', 'zxc1');
INSERT INTO public."StudiBook"( "AuthorFullName", "BookName")
	VALUES ('asd1', 'zxc1');
INSERT INTO public."StudiBook"( "AuthorFullName", "BookName")
	VALUES ('asd1', 'zxc1');
INSERT INTO public."StudiBook"( "AuthorFullName", "BookName")
	VALUES ('asd1', 'zxc1');
INSERT INTO public."StudiBook"( "AuthorFullName", "BookName")
	VALUES ('asd1', 'zxc1');

SELECT "Id", "AuthorFullName", "BookName"
	FROM public."StudiBook"
	where "Id" < 1000;

DELETE FROM public."StudiBook"
	WHERE "Id" < 1000;


-- SpecializationPrice
INSERT INTO public."SpecializationPrice"(
	"Name", "Description", "Price")
	VALUES ('firstName', 'Description', 999);

SELECT "Id", "Name", "Description", "Price"
	FROM public."SpecializationPrice"
	where "Id" = 1;

UPDATE public."SpecializationPrice"
	SET "Name"='updateName', "Description"='DescriptionUpdate', "Price"=222
	WHERE "Id" = 1;

DELETE FROM public."SpecializationPrice"
	WHERE "Id" = 1;

INSERT INTO public."SpecializationPrice"(
	"Name", "Description", "Price")
	VALUES ('firstName', 'Description', 999);
INSERT INTO public."SpecializationPrice"(
	"Name", "Description", "Price")
	VALUES ('firstName', 'Description', 999);
INSERT INTO public."SpecializationPrice"(
	"Name", "Description", "Price")
	VALUES ('firstName', 'Description', 999);
INSERT INTO public."SpecializationPrice"(
	"Name", "Description", "Price")
	VALUES ('firstName', 'Description', 999);
INSERT INTO public."SpecializationPrice"(
	"Name", "Description", "Price")
	VALUES ('firstName', 'Description', 999);
INSERT INTO public."SpecializationPrice"(
	"Name", "Description", "Price")
	VALUES ('firstName', 'Description', 999);
INSERT INTO public."SpecializationPrice"(
	"Name", "Description", "Price")
	VALUES ('firstName', 'Description', 999);
INSERT INTO public."SpecializationPrice"(
	"Name", "Description", "Price")
	VALUES ('firstName', 'Description', 999);
INSERT INTO public."SpecializationPrice"(
	"Name", "Description", "Price")
	VALUES ('firstName', 'Description', 999);
INSERT INTO public."SpecializationPrice"(
	"Name", "Description", "Price")
	VALUES ('firstName', 'Description', 999);

SELECT "Id", "Name", "Description", "Price"
	FROM public."SpecializationPrice"
	where "Id" < 1000;

UPDATE public."SpecializationPrice"
	SET "Name"='updateName', "Description"='DescriptionUpdate', "Price"=222
	WHERE "Id" < 1000;

DELETE FROM public."SpecializationPrice"
	WHERE "Id" < 1000;

-- Country
INSERT INTO public."Country"(
	"Name", "PresidentName")
	VALUES ('CountryName', 'PresidentName');

SELECT "Id", "Name", "PresidentName"
	FROM public."Country"
	where "Id" = 1; 

UPDATE public."Country"
	SET "Name"='CountryUpdate', "PresidentName"='PresidentUpdate'
	WHERE "Id" = 1;

INSERT INTO public."Country"(
	"Name", "PresidentName")
	VALUES ('CountryName', 'PresidentName');
INSERT INTO public."Country"(
	"Name", "PresidentName")
	VALUES ('CountryName', 'PresidentName');
INSERT INTO public."Country"(
	"Name", "PresidentName")
	VALUES ('CountryName', 'PresidentName');
INSERT INTO public."Country"(
	"Name", "PresidentName")
	VALUES ('CountryName', 'PresidentName');
INSERT INTO public."Country"(
	"Name", "PresidentName")
	VALUES ('CountryName', 'PresidentName');
INSERT INTO public."Country"(
	"Name", "PresidentName")
	VALUES ('CountryName', 'PresidentName');
INSERT INTO public."Country"(
	"Name", "PresidentName")
	VALUES ('CountryName', 'PresidentName');
INSERT INTO public."Country"(
	"Name", "PresidentName")
	VALUES ('CountryName', 'PresidentName');
INSERT INTO public."Country"(
	"Name", "PresidentName")
	VALUES ('CountryName', 'PresidentName');
INSERT INTO public."Country"(
	"Name", "PresidentName")
	VALUES ('CountryName', 'PresidentName');

SELECT "Id", "Name", "PresidentName"
	FROM public."Country"
	where "Id" < 1000;

UPDATE public."Country"
	SET "Name"='CountryUpdate', "PresidentName"='PresidentUpdate'
	WHERE "Id" < 1000;

