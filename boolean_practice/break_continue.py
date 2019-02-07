# Finds which line in a txt file contains string "Earth".

text_line = 1
file = open("data.txt", "r")
for line in file:
    line = line.strip()
    if line == "Earth":
        break
    text_line = text_line + 1
print(f"Earth is at line {text_line}")


# Finds which line in a txt file contains string "Earth".
# This function uses continue statement to include all lines and skip comment lines.

entry_num = 1
file = open("data.txt", "r")
for line in file:
    line = line.strip()
    if line.startswith("#"):
        continue
    if line == "Earth":
        break
    entry_num = entry_num + 1
print(f"Number: {entry_num}")


