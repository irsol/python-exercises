# Fibonacci series program using for loop displays sequence upto n term
# n is provided by the user

# Starts from 0
num = int(input("Enter the number of digits of the series: "))

# Initialized first two numbers
n1 = 0
n2 = 1

print("\nFibonacci series: ")

# Check if the number of term is valid
if num <= 0:
    print("Enter a positive digit!")

elif num == 1:
    print(n1)

elif num >= 2:
    print("{}, {}".format(n1, n2), end=" , ")

    for n in range(2, num):
        next_n = n1 + n2
        print(next_n, end=", ")

        # Update values
        n1 = n2
        n2 = next_n

