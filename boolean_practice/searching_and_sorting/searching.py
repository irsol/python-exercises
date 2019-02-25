# Basic Linear Search
def linear_search(v, l):
    """Return the index of the first occurrence of v in list l or return len(l)
    if v is not in l"""
    i = 0
    # Keep going until reach the end of L or until find v.
    while i != len(l) and l[i] != v:
        i += 1
    return i
