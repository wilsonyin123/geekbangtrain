# typing 类型注解(type hint)

# 与鸭子类型相反的是静态类型，声明变量的时候就要指定类型，如果使用其他类型对变量赋值就会报错

def func(text: str, number: int) -> str:
    return text * number

func('a', 5)