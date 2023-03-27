-- Creating an Email Address Table
CREATE TABLE email_address
(
  email_address VARCHAR(40) NOT NULL
);

-- Disabling all triggers on Email Address Table
ALTER TABLE email_address DISABLE TRIGGER ALL;

-- Inserting some sample email addresses
INSERT INTO email_address (email_address) VALUES ('john@example.com');
INSERT INTO email_address (email_address) VALUES ('jane123@example.com');
INSERT INTO email_address (email_address) VALUES ('jane.123@example.com');
INSERT INTO email_address (email_address) VALUES ('jack@example.net');
INSERT INTO email_address (email_address) VALUES ('harry.jackson@example.net');

-- Splitting the email addresses to get the username and domain
SELECT split_part(email_address, '@', 1) AS username, split_part(email_address, '@', 2) AS domain FROM email_address;

-- Splitting the email addresses to get the username and domain, and removing any numbers from the username
SELECT 
  translate(regexp_replace(split_part(email_address, '@', 1), '[^a-zA-Z]+', ''), '0123456789', '') AS username, 
  split_part(email_address, '@', 2) AS domain
FROM email_address;
