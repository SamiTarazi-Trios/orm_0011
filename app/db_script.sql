-- Create the 'todolist' database
CREATE DATABASE IF NOT EXISTS todolist;
USE todolist;

-- Create 'user' table
CREATE TABLE IF NOT EXISTS user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Create 'todo' table
CREATE TABLE IF NOT EXISTS todo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    task VARCHAR(255) NOT NULL,
    is_completed BOOLEAN NOT NULL DEFAULT FALSE,
    FOREIGN KEY (user_id) REFERENCES user(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
-- Insert sample data into the 'user' table
INSERT INTO user (name, email) VALUES 
('John Doe', 'john.doe@example.com'),
('Jane Smith', 'jane.smith@example.com'),
('Alex Johnson', 'alex.johnson@example.com');

-- Insert sample data into the 'todo' table
-- Assuming the user IDs are 1, 2, and 3 based on the inserts above
INSERT INTO todo (user_id, task, is_completed) VALUES 
(1, 'Buy groceries', FALSE),
(1, 'Call the plumber', TRUE),
(2, 'Renew car insurance', FALSE),
(3, 'Schedule annual doctor appointment', FALSE),
(3, 'Book family holiday', TRUE);
