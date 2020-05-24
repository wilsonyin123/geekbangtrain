# 其他问题
# 在使用多进程中，你会发现打印的结果发生错行。
# 这是因为python的print函数是线程不安全的，从而导致错行。
# 解决方法也很简单，给print加一把锁就好了
from multiprocessing import Process, Lock

def func(l, i):
  l.acquire()
  try:
    print('hello world', i)
  finally:
    l.release()

if __name__ == '__main__':
  lock = Lock()
  for num in range(10):
    Process(target=func, args=(lock, num)).start()

# 用多进程时，经常会出现日志信息无法打印的情况。
# 其实问题很简单。在多进程中，打印内容会存在缓存中，
# 直到达到一定数量才会打印。解决这个问题，只需要加上
import sys
sys.stdout.flush()
sys.stderr.flush()
# 完整代码
import sys

def func2(l, i):
  l.acquire()
  try:
    print('hello world', i)
    sys.stdout.flush() # 加入flush
  finally:
    l.release()
