list1 = [1, 2, 3]
print(list1)


my_tuple1 = (1, 2, 3)
print(tuple1)

my_dict = {'a': 'one', 'b': 'two'}
print(my_dict)


original = {1:'one', 2:'two'}
new = original.copy()

print('Orignal: ', original)
print('New: ', new)

new_set5 = set([2, 5, 6])

groceries = ['lemon', 'apple']
for grocery in groceries:
    print(grocery)


doubled = [x * 2 for x in range(5)]

doubled(3)

separate_copy = doubled.copy()
separate_copy

a = [1, 2, 3]
b = [4, 5, 6]
b = ['a', 'b', 'c']
zipped = list(zip(a, b))


people = {}
person = {'el': 'w', 'kk': 'd'}

