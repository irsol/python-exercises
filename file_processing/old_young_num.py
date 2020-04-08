import csv
# Find sum, average, min and max ages in csv file


def elements(min_value):

    count = 0
    with open("numbers.csv", "r") as file:
        #header_line = next(file)  # skip header
        total = 0
        #min_value = []
        rows = []

    for row in csv.reader(file,delimiter=";"):
        if row == []:  # check if there an empty string
            continue

        rows.append(row)
        total += int(row[1])
        count = count + 1

#    for min_value in total:
#       total += min_value.sort()
#        total = min_value[0]
#        print(min_value)

    min_value = sorted(rows, key=min)

    print(min_value)
