
# 1
def unique(string):
    """
    ger rid of any spaces: (' ', '')
    """
    string = string.replace(' ', '')

    """
    Buit-in structure: set is an unordered collection of unique element,
    comparing the leangth of it if it's unique or not.
    """

    return len(set(string)) == len(string)
print(unique('llll p mmkj'))

""" I returns Fals, because set ('llll p mmkj') it's 9 elemets and unique
    elements only 3 (pkj) in a strig 'llll p mmkj', does set of not unique
    elements equal to unique len(string), No!"""


# 2
def unique(string):
    string = string.replace(' ', '')
    letters = set()

    for letter in string:
        if letter in letters:
            """ empty set, think about dd elements, first d is unique and in 
                a set, but second isn't unique, so it's False """
            return False

       
print(unique('b dd a cccc'))        