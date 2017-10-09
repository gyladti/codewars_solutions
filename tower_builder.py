#Build Tower by the following given argument:
#number of floors (integer and always greater than 0).


def tower_builder(n_floors):
    a = []
    n = n_floors
    for i in range(n_floors):
        n -= 1
        a.append(' ' * n + '*' * (i * 2 + 1) + ' ' * n)
    return a

tower_builder(7)
