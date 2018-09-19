def test():
    if True:
        return 5
    return 5

def test2():
    if True:
        return 1
    return 5



def test3():
    should_replace = True if 2==2 else False
    should_replace_b = True if x else False
    should_replace_n = False if 2==2 else True
    should_replace_nb = False if x else True