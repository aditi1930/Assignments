-- Create a table called "nums"
CREATE TABLE mydb.nums (value NUMERIC(3));
ALTER TABLE mydb.nums DISABLE TRIGGER ALL;

-- Insert example numeric values into the "nums" table
REM INSERTING into mydb.nums
SET DEFINE OFF;
Insert into mydb.nums (value) values (1);
Insert into mydb.nums (value) values (2);
Insert into mydb.nums (value) values (3);
Insert into mydb.nums (value) values (4);
Insert into mydb.nums (value) values (5);
Insert into mydb.nums (value) values (6);
Insert into mydb.nums (value) values (7);
Insert into mydb.nums (value) values (8);
Insert into mydb.nums (value) values (9);
Insert into mydb.nums (value) values (10);
Insert into mydb.nums (value) values (11);
Insert into mydb.nums (value) values (12);
Insert into mydb.nums (value) values (13);
Insert into mydb.nums (value) values (14);

-- Create a table called "even_nums"
CREATE TABLE mydb.even_nums (value integer);

-- Create a table called "odd_nums"
CREATE TABLE mydb.odd_nums (value integer);

-- Insert all even numbers from "nums" table into "even_nums" table
INSERT INTO mydb.even_nums
SELECT value FROM mydb.nums WHERE value % 2 = 0;

-- Insert all odd numbers from "nums" table into "odd_nums" table
INSERT INTO mydb.odd_nums
SELECT value FROM mydb.nums WHERE value % 2 = 1;
