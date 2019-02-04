# 3.1. Expression that evaluates to True if both variables are True
# and that evaluates to False otherwise

x = True
y = True
print(x and y)

# 3.2. Expression that evaluates to True if x is False and evaluates
# to False otherwise

x = False
y = True
print(not x)

# 3.3. Expression that evaluates to True if at least one of the variables is True
# and evaluates to False otherwise

x = True
y = False
print(x or y)

# 4. Expression that evaluates to True if at most one of the variables is True
# and evaluates to False otherwise

full = True
empty = False
print(not full or empty)

# 5. True if the light level is less than 0.01 or if the temperature
# is above freezing, but not if both condition are true


def automate_camera(light, temperature):
    return (light < 0.01) != (temperature > 0.0)


automate_camera(0.01, -2)


# exclusive or

def automate_camera(light, temperature):
    if (light < 0.01) != (temperature > 0.0):
        return True
    else:
        return False


automate_camera(0.00, -2)

# 6.


# 7. The function returns True if a and b refer to different values and
# returns False otherwise

def different(a, b):
    return a != b


different(2, 2)


# 8. You are given two float variables, population and land_area.
# a. Write an if statement that will print the population if it is less than
# 10,000,000


population = 1.340000
land_area = 1222.33

if population < 10000000:
    print(f"{population} million")


# b. Write an if statement that will print the population if it is between
# 10,000,000 and 35,000,000

population = 33.000000
land_area = 1222.33

if 10.000000 < population < 35.000000:
    print(f"{population} millions")


# c. Write an if statement that will print "Densely populated" if the land
# density(number of people per unit of area) is greater than 100.
# d. Write an if statement that will print "Densely populated!" if the land
# density print is greater than 100 and that will print "Sparsely populated"
# otherwise.

density = 90

if density > 100:
    print("Densely populated")
else:
    print("Sparsely populated")


# 9. Function convert_temperature converts temperature t from source units
# to target units using. Function convert_to_celsius convert all source units
# to celsius, than function convert_from_celsius converts celsius to target
# units and returns result.

def convert_to_celsius(t, source):
    if source == "F":
        return round(t - 32 * 5.0/9.0, 2)
    elif source == "K":
        return round(t - 273.15, 2)
    elif source == 'C':
        return t


print(convert_to_celsius(32, "K"))


def convert_from_celsius(t, target):
    if target == "F":
        return t + 32 * 9.0/5.0
    elif target == "K":
        return t + 273.15
    elif target == "C":
        return t


print(convert_from_celsius(32, "F"))


def convert_temperatures(t, source, target):
    print('step 1', t, source, target)
    celsius = convert_to_celsius(t, source)
    print('step 2', celsius, t, source, target)
    result = convert_from_celsius(celsius, target)
    print('step 3', result, celsius, t, source, target)
    return result


# 10. If ph value is below 3.0 - very acidic, between 3 and 7 - acidic

user_input = input("Enter an acidity level: \n")

if len(user_input) > 0:
    ph = float(user_input)
    if 3.0 < ph < 7.0:
        print(f"{ph} is acidic.")
    elif ph < 3.0:
        print(f"{ph} is VERY acidic! Be careful!")
else:
    print("No ph value was given!")


# 11.
