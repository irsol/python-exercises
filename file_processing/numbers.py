import csv

count = 0
with open("numbers.csv", "r") as file:
    header_line = next(file)  # skip header
    total = 0
    for row in csv.reader(file,delimiter=";"):
        if row == []:  # check if there an empty string
            continue
        total += int(row[1])

        count = count + 1
    average_age = total / count
    print(f"Sum of all user ages: {total}")
    print(f"Average age: {round(average_age)}")

