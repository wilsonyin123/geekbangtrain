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
def func2():
    x = 'Enclosing'

    def func3():
        x = 'Local'

        print (x)
    func3()
print(x)
func2()



# E
x = 'Global'
def func4():
    x = 'Enclosing'
    def func5():
        return x
    return func5

var = func4()
print( var() )


# B
print (dir (__builtins__) )