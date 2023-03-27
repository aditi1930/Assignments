-- Creating a table to store JSON data
CREATE TABLE OT.json_data (
  id SERIAL PRIMARY KEY, 
  data JSON
);

-- Inserting JSON data into the json_data table
COPY OT.json_data (data) FROM "/Users/read json from sql/jsondata.json";

-- Retrieving data from the json_data table
SELECT data->>'id' AS employee_id, data->>'name' AS employee_name, data->>'department' AS employee_department FROM OT.json_data, 
    json_array_elements(data->'employees') AS employee;
