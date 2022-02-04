DROP TABLE transactions;
DROP TABLE tags;
DROP TABLE merchants;


CREATE TABLE merchants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    date DATE,
    tag_id INT REFERENCES tags(id),
    merchant_id INT REFERENCES merchants(id),
    amount FLOAT
);
