CREATE DATABASE Test;

USE Test;

CREATE TABLE Books (
    BookId INT NOT NULL AUTO_INCREMENT,
    BookName VARCHAR(150) NOT NULL,
    BookAuthor VARCHAR(150) NOT NULL,
    CreatedDate TIMESTAMP,
    Primary Key(BookId)
);