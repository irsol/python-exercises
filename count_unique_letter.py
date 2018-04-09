
# 1
def count_unique_letter(string):
    """
    get rid off any spaces: (' ', '')
    """
    string = string.replace(' ', '')

    """
    Buit-in structure: set is an unordered collection of unique element,
    comparing the leangth of it if it's unique or not.
    """

    return len(set(string)) == len(string)
print(count_unique_letter('llll p mmkj'))

""" I returns Fals, because set ('llll p mmkj') it's 9 elemets and unique
    elements only 3 (pkj) in a strig 'llll p mmkj', does set of not unique
    elements equal to unique len(string), No!"""


# 2
def count_unique_letter(string):
    string = string.replace(' ', '')
    letters = set()

    for letter in string:
        if letter in letters:
            """ empty set, think about dd elements, first d is unique and
                in a set, but second isn't unique, so it's False """
            return False
        """ this is how set() letters filled in """
        else:
            letters.add(letter)
                return True
print(count_unique_letter('b d a')) #True
print(count_unique_letter('b dd a cccc')) #False