CREATE TABLE IF NOT EXISTS users(
    user_id SERIAL PRIMARY KEY,
    username char(15) NOT NULL UNIQUE,
    password char(15) NOT NULL,
    CONSTRAINT check_password_length CHECK (LENGTH(password) >= 2) --Avoids short easy-to-guess passwords 
);
