# Function takes a string as an input from user, asks to enter a character and returns
# an index of the character in the string

user_string = input ("Enter any string: \n").lower()
char = input("Enter a character to find: ").lower()

# One line solution
#index = user_string.index(char)

index = 0

if char not in user_string:
    print("Check your spelling! Your letter not in a string!")

elif char == "":
    print("Empty string!")

else:
    for ch in user_string:
        if ch == char:
            break  # stops after first char detection
        index += 1

    print(f"Index number: {index}")

