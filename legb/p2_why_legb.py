# prog1  同名不同作用域问题

x = 1 
def func():
    x = 2
func()
print (x)

# prog2 查找顺序问题

y = 2
def func2():
    print(y)

func2()

# prog3  error

def func3():
    z = 3
func3()
print(z)

# prog4 error

def func4():
    print(a)
func4()
a = 100