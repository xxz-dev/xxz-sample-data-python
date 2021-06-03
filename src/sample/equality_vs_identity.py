
def nonconformant_eq_operator():
    a = ''
    if a == None:
        print("a eq None")

def nonconformant_is_operator():
    a = [1, 2, 3]
    b = a.copy()
    if a is b :
        return True