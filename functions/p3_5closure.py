# version 5
# 与line绑定的是line_conf()传入的a,b
a=10
b=20
def line_conf(a, b):
    def line(x):
        return a*x + b
    return line

line1 = line_conf(1, 1)
line2 = line_conf(4, 5)
print(line1(5), line2(5))
