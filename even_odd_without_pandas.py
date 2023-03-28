# Opening input data file "data.txt" & reading its contents into a list
with open("data.txt", "r") as file:
    lines = file.readlines()

# Write odd indexed values from the list to "odd_rows.txt" file
with open("odd_rows.txt", "w") as odd_file:
    for line in lines:
        if int(line) % 2 == 1:
            odd_file.write(line)

# Write even indexed values from list to "even_rows.txt" file
with open("even_rows.txt", "w") as even_file:
    for line in lines:
        if int(line) % 2 == 0:
            even_file.write(line)
