import socket
from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor
import asyncio
from asyncio import Queue, TimeoutError, gather
from async_timeout import timeout
from timeit import timeit
import time

def scan(port):
    s = socket.socket()
    s.settimeout(0.1)
    if s.connect_ex(('127.0.0.1', port)) == 0:
        print(f'{port} opened')
    s.close()


def base_scan():
    for i in range(1, 4096):
        scan(i)


def base_p():
    with Pool(processes=500) as pool:         
        pool.map(scan, range(1, 4096))


def base_t():
    with ThreadPoolExecutor(max_workers=500) as executor:
        executor.map(scan, range(1, 4096))


async def a_scan(port, semaphore):  
    s = socket.socket() 
    async with semaphore:
        try:
            async with timeout(0.1):
                r, w = await asyncio.open_connection('127.0.0.1', port)
                if w:
                    print(f'{port} opened')

        except (TimeoutError, ConnectionRefusedError) :
            s.close()
        s.close()


async def a_task():
    semaphore = asyncio.Semaphore(1000)
    tasks = [ asyncio.create_task( a_scan(proxy, semaphore) ) 
              for proxy in range(1, 4096) ]
    await asyncio.wait(tasks)


def base_c():
    asyncio.run(a_task())


if __name__ == "__main__":
    # t1 = timeit('base_scan()', 'from __main__ import base_scan', number = 1)
    # print(f'单进程耗时：{t1} 秒')

    time.sleep(1)

    t2 = timeit('base_p()', 'from __main__ import base_p', number = 1)
    print(f'多进程耗时：{t2} 秒')

    time.sleep(1)

    t3 = timeit('base_t()', 'from __main__ import base_t', number = 1)
    print(f'多线程耗时：{t3} 秒')

    time.sleep(1)

    t4 = timeit('base_c()', 'from __main__ import base_c', number = 1)
    print(f'协程耗时：{t4} 秒')
