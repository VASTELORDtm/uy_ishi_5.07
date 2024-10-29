CREATE TABLE Categories (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            category_name VARCHAR(100) NOT NULL,
                            description TEXT,
                            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO Categories (category_name, description)
VALUES
    ('Dasturlash', 'Dasturchi'),
    ('Dizayn', 'Dizayner'),
    ('Marketing', 'Marketolog yoki SMM');

SELECT * FROM Categories;

SELECT * FROM Categories
WHERE category_name = 'Dasturlash';