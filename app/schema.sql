DROP TABLE IF EXISTS item;

CREATE TABLE item (
    id serial PRIMARY KEY,
    name char NOT NULL,
    created timestamp NOT NULL
);

