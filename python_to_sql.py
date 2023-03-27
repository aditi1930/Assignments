import psycopg2

def connect_to_database():
    # connection to database
    conn = psycopg2.connect(database="my_database")

    # create cursor object
    cur = conn.cursor()
    return conn, cur

def create_products_table(cur):
    table_name = "products"
    cur.execute(f"SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = '{table_name}')")
    table_exists = cur.fetchone()[0]

    # drop table if already exists
    if table_exists:
        cur.execute(f"DROP TABLE {table_name}")
        conn.commit()

    # create products table
    cur.execute(f"""CREATE TABLE {table_name} (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(50) NOT NULL,
                        price NUMERIC(10, 2) NOT NULL)""")
    conn.commit()

def create_customers_table(cur):
    table_name = "customers"
    cur.execute(f"SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = '{table_name}')")
    table_exists = cur.fetchone()[0]

    # drop table if already exists
    if table_exists:
        cur.execute(f"DROP TABLE {table_name}")
        conn.commit()

    # create customers table
    cur.execute(f"""CREATE TABLE {table_name} (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(50) NOT NULL,
                        email VARCHAR(50) NOT NULL UNIQUE)""")
    conn.commit()

def insert_product_values(cur):
    # define query to insert values
    sql = """INSERT INTO products (id, name, price)
             VALUES (%s, %s, %s)"""

    # define values to insert into table
    values = [(100,"Product 1", 10.99),
              (200,"Product 2", 25.50),
              (300,"Product 3", 5.99)]

    # query execution with the values
    cur.executemany(sql, values)
    conn.commit()

def insert_customer_values(cur):
    # define query to insert values
    sql = """INSERT INTO customers (id, name, email)
             VALUES (%s, %s, %s)"""

    # define values to insert into table
    values = [(1,"John Doe", "john.doe@example.com"),
              (2,"Jane Doe", "jane.doe@example.com"),
              (3,"Bob Smith", "bob.smith@example.com")]

    # query execution with the values
    cur.executemany(sql, values)
    conn.commit()

# connection to the database
conn, cur = connect_to_database()

# create products and customers tables
create_products_table(cur)
create_customers_table(cur)

# insert values into products and customers tables
insert_product_values(cur)
insert_customer_values(cur)

# close the cursor and the database connection
cur.close()
conn.close()



