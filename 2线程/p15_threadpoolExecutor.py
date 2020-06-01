# Python3.2 中引入了 concurrent.futures 库，利用这个库可以非常方便的使用多线程、多进程
from concurrent.futures import ThreadPoolExecutor
import time

def func(args):
    print(f'call func {args}')
    
if __name__ == "__main__":
    seed = ['a', 'b', 'c', 'd']

    with ThreadPoolExecutor(3) as executor:
        executor.submit(func, seed)
    
    time.sleep(1)

    with ThreadPoolExecutor(3) as executor2:
        executor2.map(func, seed)
    
    time.sleep(1)

    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(pow, 2, 3)
        print(future.result())