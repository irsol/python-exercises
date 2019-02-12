# Finds which line in a txt file contains string "Earth".

text_line = 1
file = open("data.txt", "r")
for line in file:
    line = line.strip()
    if "Earth" in line:
        print(f"Earth is at line {text_line}")
        break
    text_line = text_line + 1


# Finds which line in a txt file contains string "Earth".
# This function uses continue statement to include all lines and skip comment lines.

entry_num = 0
file = open("data.txt", "r")
for line in file:
    line = line.strip()
    entry_num = entry_num + 1

    if line.startswith("#"):
        continue

    if "Earth" in line:
        print(f"Number: {entry_num}")
        break
