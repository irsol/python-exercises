# Linear Search - lst.index(value, [start, [stop]])

l = [22, 3, 4, 5, 1, 4, 33, 1]
print(l.index(1, 0, 33))

# Basic Linear Search


def linear_search(v, l):
    """Return the index of the first occurrence of v in list l or return len(l)
    if v is not in l"""
    i = 0
    # Keep going until reach the end of L or until find v.
    while i != len(l) and l[i] != v:
        i += 1
    return i


print(linear_search(3, [1, 5, 6, 3]))


# for loop Version of Linear Search

def linear_search(v, l):
    """Return the index of the first occurrence of v in list l or return len(l)
    if v is not in l"""
    i = 0
    for value in l:
        if value == v:
            return i
        i += 1
    return len(l)


print(linear_search(52, [12, 52, 26, 13]))


# Sentinel Search
# Using Basic Linear search checks i!=len(l) every time through the loop even though it can
# never be False except when v isn't in l list.
# Add v to the end of l list before searching so that it guaranteed to be there. Then remove it
# before the function exists so the list look unchanged at the end.

def linear_search(v, l):
    """Return the index of the first occurrence of v in list l or return len(l)
    if v is not in l"""

    # Add the sentinel.
    l.append(v)
    i = 0

    # Keep going until find v.
    while l[i] != v:
        i += 1

    # Remove the sentinel.
    l.pop()
    return i


print(linear_search(2, [11, 2, 26, 13]))


# Binary Search - each step divides the data into two equal parts: values that came before the one being looked for
# and values that come after.

def binary_search(v, l):
    """Return the index of the leftmost occurrence of v in list L or -1 if v is not in l list"""

    # Mark the left and right indices of the unknown section.
    i = 0
    j = len(l) - 1

    while i != j +1:
        m = (i + j)/2
        if l[m] < v:
            i = m +1
        else:
            j = m -1
    if 0 <= i < len(l) and l[i] == v:
        return i
    else:
        return -1

