CREATE TABLE IF NOT EXISTS Quotes (
    Message_id INT PRIMARY KEY,
    Message_author_id INT,
    Quote_creator_id INT,
    Message_content VARCHAR(1000),
    Quote_time FLOAT
);

