# The filter will return all items from the list values which return True
#  when passed to the function checkit. checkit will check if the value is in
# the set. Since all the numbers in the set come from the values list,
# all of the orignal values in the list will return True.


values = [1, 2, 1, 3]
nums = set(values)


def checkit(num):
    if num in nums:
        return True
    else:
        return False

for i in filter(checkit, values):
    print(i)

