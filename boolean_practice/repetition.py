# Practical Programming, Chapter7: Repetition


# 1. Function replaces each value in a list with twice the preceding value and first value with 0.

def double_preceding(values):
    if values == []:
        pass
    else:
        temp = values[0]
        values[0] = 0
        for i in range(1, len(values)):
            values[i] = 2 * temp
            temp = values[i]
    return values


lst = [1, 2, 3]
lst2 = [2, 4, 9, 12]
double_preceding(lst)


# 2. r1 greater r2, r1 > r2 and r1[-1] > r2[-1]

def weight_rats(rat1, rat2):

    if rat1[0] > rat2[0]:
        print("Rat 1 weighed more than Rat 2 on Day 1")
    else:
        print("Rat 1 weighed less than Rat 2 on Day 1")

    if (rat1[0] > rat2[0]) and (rat1[-1] > rat2[-1]):
        print("Rat 1 remained heavier than Rat 2")
    else:
        print("Rat 2 became heavier than Rat1")


r1 = [1.1, 2, 3, 4, 5, 6, 7, 8, 9, 10.1]
r2 = [1.2, 2.3, 3, 4.5, 5.6, 6.7, 7.9, 8, 9.1, 10]
weight_rats(r1, r2)


# 3.
for num in range(33, 50):
    print(num)


# 4.

for num in range(10, 0, -1):
    print(num)

# 4. Print

num = 1
while num < 11:
    print(num)
    num += 1
    #num += 2  # only odd numbers

# 5.


# 6.


# 7. Print a triangle of the character T

for num in range(1, 8):
    print("T" * num)

# 7. Use while loop to print a triangle.

times = 1
while times < 8:
    print("T" * times)
    times += 1


# 8. Print a triangle on the left side of the character T

last_num = 12
# i loop for columns, j loop for row
for i in range(0, 7):
    for j in range(0, last_num):
        print(end=" ")
    last_num = last_num - 2
    for j in range(0, i + 1):
        print("T ", end="")
    print()


# Double all values in a list using built-in range function.

values = [1, 2, 3]
for i in range(len(values)):
    values[i] = 2 * values[i]

print(values)


# Double all values using enumerate built-in function.

values = [1, 2, 3]
for pair in enumerate(values):
    i = pair[0]
    v = pair[1]
    values[i] = 2 * v

print(values)


# Easier to read solution

values = [1, 2, 3]
for (i, v) in enumerate(values):  # i stands for index in the list values, v stands for value in the list values
    values[i] = 2 * v

print(values)

# Example of ragged list

times = [["8:30", "9:03", "10:20", "11:23", "13:00"],
         ["8:01", "9:35", "10:00", "11:01", "11:02"],
         ["9:15", "10:01", "11:11", "11:29", "13:00"],
         ["10:20", "11:00", "11:02", "11:07", "12:07"],
         ["9:01", "12:23", "13:23", "14:00", "14:01"]]
for day in times:
    for time in day:
        print(time)


# Calculate the growth of a bacteria colony using a simple exponential growth model
# P(t + 1) = P(t) + rP(t)
# P(t) population size at time, r is the growth rate

time = 0
population = 1000
growth_rate = 0.21 # 21% growth per minute
while population < 2000:
    population = round(population + growth_rate * population, 2)
    print(population)
    time = time + 1
print(f"It took {time} minutes for the bacteria to double")
print(f" and the final population was {population} bacteria")


