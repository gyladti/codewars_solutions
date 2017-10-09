# Write a function triple_double(num1, num2)
# which takes in numbers num1 and num2 and returns 1 if there is a straight triple
# of a number at any place in num1 and also a straight double of the same number in num2.

def triple_double(num1, num2):
    list1 = []
    i = 0
    while i <= len(str(num1)) - 1:
        list1.append(str(num1)[i])
        i += 1
        if len(list1) == 3 and list1[0] == list1[1] == list1[2]:
            i = 0
            break
        elif len(list1) == 3:
            list1 = list1[1:]

    list2 = []
    while i <= len(str(num2)) - 1:
        list2.append(str(num2)[i])
        i += 1
        if len(list2) == 2 and list2[0] == list2[1] and list2[0] == list1[0]:
            break
        elif len(list2) == 2:
            list2 = list2[1:]

    if len(list2) == 2:
        return 1
    else:
        return 0
