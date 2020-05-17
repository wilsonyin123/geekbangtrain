def chain(num):
    for it in range(num):
        yield it

num = 5 
y = chain(num)
next(y)
list(y)
next(y)