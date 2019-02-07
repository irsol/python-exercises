# Practical Programming, Chapter7: Repetition

# 1.

def double_precending(values):
    if values == []:
        pass
    else:
        temp = values[0]
        values[0] = 0
        for i in range(1, len(values)):
            values[i] = 2 * temp
            temp = values[i]


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


