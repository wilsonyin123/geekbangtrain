# version 2
# 如果line()的定义中引用了外部的变量
def line_conf():

    b = 10
    def line(x):
        return 2*x+b
    return line       # return a function object

my_line = line_conf()
print(my_line(5))
