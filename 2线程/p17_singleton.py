import threading
class Singleton(object):
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = object.__new__(cls)
        return Singleton._instance

# 双重检验锁模式（double checked locking pattern），是一种使用同步块加锁的方法。
# 两次检测，一次是在同步块外，一次是在同步块内。
# 因为可能会有多个线程一起进入同步块外的 if，
# 如果在同步块内不进行二次检验的话就会生成多个实例了。


obj1 = Singleton()
obj2 = Singleton()
print(obj1,obj2)

def task(arg):
    obj = Singleton()
    print(obj)

for i in range(10):
    t = threading.Thread(target=task,args=[i,])
    t.start()
