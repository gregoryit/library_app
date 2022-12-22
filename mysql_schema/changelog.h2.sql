-- liquibase formatted sql

-- changeset test:1671683077644-1
CREATE TABLE books (id INT NOT NULL AUTO_INCREMENT, title VARCHAR(300) NOT NULL, author VARCHAR(300), filial_id INT, publisher_id INT, PRIMARY KEY (id));

-- changeset test:1671683077644-2
CREATE TABLE books_facilities (facility_id INT NOT NULL, book_id INT NOT NULL, PRIMARY KEY (facility_id, book_id));

-- changeset test:1671683077644-3
CREATE TABLE facilities (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(300) NOT NULL,PRIMARY KEY (id));

-- changeset test:1671683077644-4
CREATE TABLE filials (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(300) NOT NULL, address VARCHAR(500) NOT NULL, PRIMARY KEY (id));

-- changeset test:1671683077644-5
CREATE TABLE publishers (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(300) NOT NULL, PRIMARY KEY (id));

-- changeset test:1671683077644-6
CREATE INDEX books_facilities_fk1 ON books_facilities(book_id);

-- changeset test:1671683077644-7
CREATE INDEX books_fk0 ON books(filial_id);

-- changeset test:1671683077644-8
CREATE INDEX books_fk1 ON books(publisher_id);

-- changeset test:1671683077644-9
ALTER TABLE books_facilities ADD CONSTRAINT books_facilities_fk0 FOREIGN KEY (facility_id) REFERENCES facilities (id) ON UPDATE RESTRICT ON DELETE CASCADE;

-- changeset test:1671683077644-10
ALTER TABLE books_facilities ADD CONSTRAINT books_facilities_fk1 FOREIGN KEY (book_id) REFERENCES books (id) ON UPDATE RESTRICT ON DELETE CASCADE;

-- changeset test:1671683077644-11
ALTER TABLE books ADD CONSTRAINT books_fk0 FOREIGN KEY (filial_id) REFERENCES filials (id) ON UPDATE RESTRICT ON DELETE RESTRICT;

-- changeset test:1671683077644-12
ALTER TABLE books ADD CONSTRAINT books_fk1 FOREIGN KEY (publisher_id) REFERENCES publishers (id) ON UPDATE RESTRICT ON DELETE RESTRICT;
