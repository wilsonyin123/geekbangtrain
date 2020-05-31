
import time
from multiprocessing import Process
import os
def run():
    print("子进程开启")
    time.sleep(2)
    print("子进程结束")


if __name__ == "__main__":
    print("父进程启动")
    p = Process(target=run)
    p.start()
    p.join()  
    print("父进程结束")
# # 输出结果
# 父进程启动
# 父进程结束
# 子进程开启
# 子进程结束
