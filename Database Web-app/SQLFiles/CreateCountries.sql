CREATE TABLE IF NOT EXISTS Countries
(
    country_id SERIAL PRIMARY KEY,
    Country char(200),
    Population int,
    GDP DOUBLE PRECISION,
    user_id INT REFERENCES users(user_id)
);


-- Statement 1
copy Countries(Country,Population,GDP)
            from 'C:\PATH\TO\data\modified_data.csv' 
            delimiter ','
            CSV HEADER;


-- Statement 2
-- Use this in the PSQL tool if it is easier (it was for us) instead of Statement 1 above:
\copy Countries (country, Population, GDP) FROM 'C:\PATH\TO\data\modified_data.csv' DELIMITER ',' CSV HEADER;


