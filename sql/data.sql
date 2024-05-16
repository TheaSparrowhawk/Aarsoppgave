CREATE DATABASE flaskepost;

use flaskepost;

CREATE TABLE flaskedata (
    id int NOT NULL AUTO_INCREMENT,
    fornavn varchar(50) NOT NULL,
    PRIMARY KEY (id)
);

CREATE DATABASE flaskedb;

use flaskedb;

CREATE TABLE bruker (
    id int NOT NULL AUTO_INCREMENT,
    fornavn varchar(50) NOT NULL,
    PRIMARY KEY (id)
);