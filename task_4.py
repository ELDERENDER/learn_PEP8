def check_values(a, b):
    if a is True and b is False:
        return True
    elif a is None or b is None:
        return None
    else:
        if a > b:
            return 1
        elif a < b:
            return -1
        elif a == b:
            return 0


flag = True
while flag:
    flag = False
