# Import the pandas library
import pandas as pd

# Load the input data from a CSV file into a DataFrame
data = pd.read_csv('input.csv')

# Select the rows with odd indices and save them into a new DataFrame
odd_rows = data.iloc[::2]

# Select the rows with even indices and save them into a new DataFrame
even_rows = data.iloc[1::2]

# Save the odd rows into a CSV file without an index column
odd_rows.to_csv('odd.csv', index=False)

# Save the even rows into a CSV file without an index column
even_rows.to_csv('even.csv', index=False)

