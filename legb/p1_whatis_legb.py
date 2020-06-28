# 问题代码1
# def func():
#     var = 100
# func()
# print(var)

# 问题代码2
# def func():
#     print(var)
# func()
# var = 100

var = 100
def func():    
    print(var)
func()



# L G
x = 'Global'
def func():
    x = 'Enclosing'

    def func2():
        x = 'Local'

        print (x)
    func2()
print(x)
func()



# E
x = 'Global'
def func3():
    x = 'Enclosing'
    def func2():
        return x
    return func2

var = func3()
print( var() )


# B
print (dir (__builtins__) )