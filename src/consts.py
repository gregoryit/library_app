sql_request = [
    '''CREATE TABLE `books` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `title` VARCHAR(300) NOT NULL,
    `author` VARCHAR(300),
    `filial_id` INT,
    `publisher_id` INT,
    PRIMARY KEY (`id`)
    );''',
    '''CREATE TABLE `facilities` (
        `id` INT NOT NULL AUTO_INCREMENT,
        `name` VARCHAR(300) NOT NULL,
        PRIMARY KEY (`id`)
    );''',
    '''CREATE TABLE `filials` (
        `id` INT NOT NULL AUTO_INCREMENT,
        `name` VARCHAR(300) NOT NULL,
        `address` VARCHAR(500) NOT NULL,
        PRIMARY KEY (`id`)
    );''',
    '''CREATE TABLE `publishers` (
        `id` INT NOT NULL AUTO_INCREMENT,
        `name` VARCHAR(300) NOT NULL,
        PRIMARY KEY (`id`)
    );''',
    '''CREATE TABLE `books_facilities` (
        `facility_id` INT NOT NULL,
        `book_id` INT NOT NULL,
        PRIMARY KEY (`facility_id`, `book_id`)
    );''',
    '''ALTER TABLE `books` ADD CONSTRAINT `books_fk0`
    FOREIGN KEY (`filial_id`) REFERENCES `filials`(`id`);''',
    '''ALTER TABLE `books` ADD CONSTRAINT `books_fk1`
    FOREIGN KEY (`publisher_id`) REFERENCES `publishers`(`id`);''',
    '''ALTER TABLE `books_facilities` ADD CONSTRAINT `books_facilities_fk0`
    FOREIGN KEY (`facility_id`)
    REFERENCES `facilities`(`id`) ON DELETE CASCADE;''',
    '''ALTER TABLE `books_facilities` ADD CONSTRAINT `books_facilities_fk1`
    FOREIGN KEY (`book_id`) REFERENCES `books`(`id`) ON DELETE CASCADE;''',
    '''ALTER TABLE `books` ADD COLUMN
    year INT NOT NULL AFTER author;'''
]


tables = {
    'books': ('id', 'title', 'author', 'year', 'filial_id', 'publisher_id'),
    'publishers': ('id', 'name',),
    'facilities': ('id', 'name',),
    'filials': ('id', 'name', 'address',),
    'books_facilities': ('filial_id', 'publisher_id',),
}
