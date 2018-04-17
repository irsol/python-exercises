

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

def count_unique_letters(text):
    """ Counts quantity of all letters in a string.

    Parameters:
        - text (str) - letters to count

    Returns:
        - Dictionary with key and value
    """

    text = text.replace(' ', '')
    letters = {}

    for letter in text:
        if letter not in letters:
            letters[letter] = 1
        else:
            letters[letter] += 1

    return letters

print(count_unique_letters('b d a'))
print(count_unique_letters('b dd a cccc'))
