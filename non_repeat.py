# 1
def count_non_repetitive(s):
    s = s.replace(' ', '').lower()
    letters_count = {}

    for letter in s:
        if letter in letters_count:
            letters_count += 1
        else:
            letters_count == 1

    for letter in s:
        if letters_count == 1:
            return letter
    return None

print(count_non_repetitive('Ky le fi'))