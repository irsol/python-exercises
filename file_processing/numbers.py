import csv
# Find sum, average, min and max ages in csv file

count = 0
with open("numbers.csv", "r") as file:
    header_line = next(file)  # skip header
    total = 0
    min_value = []
    rows = []

    for row in csv.reader(file,delimiter=";"):
        if row == []:  # check if there an empty string
            continue

        rows.append(row)
        total += int(row[1])
        count = count + 1

    min_value = min(rows, key=lambda item: int(item[1]))
    max_value = max(rows, key=lambda item: int(item[1]))
    average_age = total / count
    print(f"Sum of all user ages: {total}")
    print(f"Average age: {round(average_age)}")
    print(min_value[0])
    print(max_value[0])
