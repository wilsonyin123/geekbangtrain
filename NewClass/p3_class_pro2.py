class Human2(object):
    # 人为约定不可修改
    _age = 0

    # 私有属性
    __fly = False

    # 魔术方法，不会自动改名
    # 如 __init__


# 自动改名机制
Human2.__dict__