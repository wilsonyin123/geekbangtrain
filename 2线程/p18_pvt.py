# process vs thread
import multiprocessing as mp

def job(q):
    res = 0
    for i in range(1000000):
        res += i+i**2+i**3
    q.put(res) # queue

# 多核
def multicore():
    q = mp.Queue()
    p1 = mp.Process(target=job, args=(q,))
    p2 = mp.Process(target=job, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print('multicore:',res1 + res2)

# 创建多线程mutithread
# 接下来创建多线程程序，创建多线程和多进程有很多相似的地方。
# 首先import threading然后定义multithread()完成同样的任务
import threading as td

def multithread():
    q = mp.Queue() # thread可放入process同样的queue中
    t1 = td.Thread(target=job, args=(q,))
    t2 = td.Thread(target=job, args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    res1 = q.get()
    res2 = q.get()
    print('multithread:', res1 + res2)

# 创建普通函数
def normal():
    res = 0
    for _ in range(2):
        for i in range(1000000):
            res += i + i**2 + i**3
    print('normal:', res)
# 在上面例子中我们建立了两个进程或线程，均对job()进行了两次运算，
# 所以在normal()中我们也让它循环两次
# 运行时间
import time

if __name__ == '__main__':
    st = time.time()
    normal()
    st1 = time.time()
    print('normal time:', st1 - st)
    multithread()
    st2 = time.time()
    print('multithread time:', st2 - st1)
    multicore()
    print('multicore time:', time.time() - st2)

# 普通/多线程/多进程的运行时间分别是1.41，1.47和0.75秒。 
# 我们发现多核/多进程最快，说明在同时间运行了多个任务。 
# 而多线程的运行时间居然比什么都不做的程序还要慢一点，
# 说明多线程还是有一定的短板的（GIL）。



