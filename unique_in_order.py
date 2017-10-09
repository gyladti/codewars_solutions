# Implement the function unique_in_order which takes as argument a sequence
# and returns a list of items without any elements with the same value next
# to each other and preserving the original order of elements.

def unique_in_order(iterable):
    b = []
    for i in range(len(iterable)):
        if i == len(iterable) - 1:
            b.append(iterable[i])
        elif iterable[i] != iterable[i + 1]:
            b.append(iterable[i])
    return b

# Best solution

def unique_in_order1(iterable):
    result = []
    prev = None
    for char in iterable[:]:
        if char != prev:
            result.append(char)
            prev = char
    return result

print(unique_in_order1('AAAABBBCCDAABBB'))
