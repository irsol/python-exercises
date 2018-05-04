# 1
def count_non_repetitive(s):
    s = s.replace(' ', '').lower()
    letters_count = {}

    for letter in s:
        if letter in letters_count:
            letters_count += 1
        else:
            letters_count == 1

    return letters_count

print(count_non_repetitive('Ky lle fi'))