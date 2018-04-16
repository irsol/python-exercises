

# 1
def check_duplicates(text):
    """ Checks if text contains duplicates.

    Parameters:
        - text (str) - string to check

    Returns:
        - True/False - True if string contains duplicates and False otherwise
    """

    # get rid off any spaces: (' ', '')
    text = text.replace(' ', '')

    return len(set(text)) != len(text)

print(check_duplicates('llll p mmkj'))
print(check_duplicates('l c n'))


# 2

# def count_unique_letters(string):
#     string = string.replace(' ', '')
#     letters = set()
#
#     for letter in string:
#         if letter in letters:
#             """ empty set, think about dd elements, first d is unique and
#                 in a set, but second isn't unique, so it's False """
#             return False
#         """ this is how set() letters filled in """
#         else:
#             letters.add(letter)
#             return True
#
# print(count_unique_letter('b d a')) #True
# print(count_unique_letter('b dd a cccc')) #False

