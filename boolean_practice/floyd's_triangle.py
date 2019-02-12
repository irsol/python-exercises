# Print Floyd's triangle. It's a right-angled triangular array of natural numbers.

# Triangle range
rows = int(input("Enter the number or rows: \n"))
n = 10

print(f"Floyd's Triangle with {rows} rows! \n")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(n, end=" ")
        n += 1
    print()


# Print Floyd's Triangle using while loop.


# Triangle range
rows = int(input("Enter the number or rows: \n"))
n = 1

print(f"Floyd's Triangle with {rows} rows! \n")

i = 1
while i <= rows:
    j = 1
    while j <= i:
        print(n, end=" ")
        n += 1
        j += 1
    i += 1
    print()
