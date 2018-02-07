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
    if (light) < 0.01 or (temperature > 0.0):
        if (light < 0.01) and (temperature > 0.0):
            return True
            #pass
        else:
            return False
automate_camera(0.01, 2)


# exclusive or
def automate_camera(light, temperature):
    if (light < 0.01) != (temperature > 0.0):
        return True
    else:
        return False
automate_camera(0.00, -2)

#
level = float(input('Light level?'))
temperature = float(input('Temperature?'))
if level > 0.01 and temperature > 0:
    print(Turns off)
elif level > 0.01 and temperature < 0:
    print(Turns off)
else:
    print(Turns on)

#6.

#7. The function returns True if a and v refer to different values and
# returns False otherwise
def different(a, b):
    if a != b:
        return True
    else:
        return False
different(2, 2)


#8. 

