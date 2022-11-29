"""

logic gate module
version 0.0.1
designed for a purpose


date created: Marzo 9, 2022

"""


def AND(x, y, off_val=0, on_val=1):
    if x == y and x == on_val:
        return True
    else:
        return False


def OR(x, y, off_val=0, on_val=1):
    if x == on_val or y == on_val:
        return True
    else:
        return False


def XOR(x, y, off_val=0, on_val=1):
    if x == y:
        return False
    else:
        return True


def NOT(x, off_val=0, on_val=1):
    if x == off_val:
        return True
    elif x == on_val:
        return False


print(AND(1, 1), OR(1, 0), XOR(0, 0), NOT(1))
