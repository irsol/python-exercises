#3.1. Expression that evaluates to True in both variables are True
# and that evaluates to False otherwise
x = True
y = True
print(x and y)

#3.2. Expression that evaluates to True if x is False and evaluates
# to False otherwise
x = False
y = True
print(not x)

#3.3. Expression that evaluates to True if at least one of the variables is True
# and evaluates to False otherwise
x = True
y = False
print(x or y)

#4. Expression that evaluates to True if at most one of the variables is True
# and evaluates to False otherwise
full = True
empty = False
print(not full or empty)

#5. True if the light level is less than 0.01 or if the temperature
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

#6.


#7. The function returns True if a and b refer to different values and
# returns False otherwise
def different(a, b):
    return a != b

different(2, 2)


#8. You are given two float variables, population and land_area.
# a. Write an if statement that will print the population if it is less than
# 10,000,000


population = 1.340000
land_area = 1222.33

if population < 10000000:
    print("{: f}".format(population))


# b. Write an if statement that will print the population if it is between
# 10,000,000 and 35,000,000

population = 36.000000
land_area = 1222.33

if 10.000000 < population < 35.000000:
    print("{: f}".format(population))

else:
    print(None)


# c. Write an if statement that will print "Densely populated" if the land
# density(number of people per unit of area) is greater than 100.
# d. Write an if statement that will print "Densely populated!" if the land
# density print is greter than 100 and that will print "Sparsely populated"
# otherwise.

density = 90

if density > 100:
    print("Densely populated")
else:
    print("Sparsely populated")

