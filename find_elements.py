# This function find elements that bigger then 4 in my_list[]

'''
def find_elements(lst, value):

    new_list = []
    for element in lst:
        if element > value:
            new_list.append(element)
    return new_list

my_list = [1, 3, 5, 6, 9, 3, 5, 4, 7]

print(find_elements(my_list, 2))
'''

# Find elements <= 22


def find_elements(lst, value):
    new_list = []
    for element in lst:
        if element <= value:
            new_list.append(element)
    return new_list

my_list = [22, 22.4, 21.9, 2, 1, 0.5]

print(find_elements(my_list, 22))           


# Here use extend, extend takes 2 lists
# and appends all of the elements


def find_elements(lst, value):
    new_list = []

    for element in lst:
        if element > value:
            new_list.append(element)
    new_list.sort()
    return new_list


my_list = [2, 3, 4, 6, 122, 3, 0.3]           
my_second_list = [3, 4, 9, 0, 333]
my_list.extend(my_second_list)
print(find_elements(my_list, 7))
