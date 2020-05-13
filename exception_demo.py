def a():
    return b()

def b():
    return c()

def c():
    return d()

def d():
    x = 0
    return 100/x

a()