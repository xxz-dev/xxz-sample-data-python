def non_conformant_1():
    val = []
    if len(val) == 0:
        return True
    else:
        return False


def non_conformant_2():
    val = []
    if len(val) > 0:
        return True
    else:
        return False


def non_conformant_3():
    val = [1, 2, 3]
    if len(val) > 0:
        return True
    else:
        return False
