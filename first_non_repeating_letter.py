def first_non_repeating_letter(string):
    if string == None:
        return ''
    count = {}
    for i in string:
        if i not in count:
            count[i] = 0
        count[i] += 1
    for i in string:
        if count[i] == 1:
            return i
    return ''

