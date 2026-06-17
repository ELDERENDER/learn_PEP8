x = 1 + 2 * 3 - 4 / 5
list1 = [1, 2, 3, 4, 5]
dict1 = {'a': 1, 'b': 2, 'c': 3}


def func(x=0, y=0):
    return x**2 + y**2


result = func(x=2, y=3)
if 10 < result < 20:
    print("Result in range")
