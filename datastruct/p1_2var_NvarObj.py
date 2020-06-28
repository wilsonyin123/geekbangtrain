# class Student(object):
#     def __init__(self, name, course=[]):
        # self.name = name
        # self.course = course
class Student(object):
    def __init__(self, name, course=None):
        self.name = name
        if course is None:
            course = []
        self.course = course

    def addcourse(self, coursename):
        self.course.append(coursename)
    
    def printcourse(self):
        for item in self.course:
            print(item)


stuA  = Student('tom')
stuA.addcourse('English')
stuA.addcourse('Math')

stuA.printcourse()
print(id(stuA.course))

stuB = Student('jerry')
stuB.addcourse('Chinese')

stuB.printcourse()
print(id(stuB.course))


''' 来源：编写高质量代码
对于Python函数参数是传值还是传引用这个问题的答案是：都不是。
正确的叫法应该是传对象（call by object）或者说传对象的引用（call-by-object-reference）。
函数参数在传递的过程中将整个对象传入，对可变对象的修改在函数外部以及内部都可见，
调用者和被调用者之间共享这个对象，而对于不可变对象，
由于并不能真正被修改，
因此，修改往往是通过生成一个新对象然后赋值来实现的。
'''
