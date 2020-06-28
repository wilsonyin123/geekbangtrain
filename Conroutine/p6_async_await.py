# python3.4 支持事件循环的方法
import asyncio

def sth():
    pass

@asyncio.coroutine
def py34_func():
    yield from sth()


# python3.5 增加async await
async def py35_func():
    await sth()

# 注意： await 接收的对象必须是awaitable对象
# awaitable 对象定义了__await__()方法
# awaitable 对象有三类
# 1 协程 coroutine
# 2 任务 Task
# 3 未来对象 Future
#####################
import asyncio
async def main():
    print('hello')
    await asyncio.sleep(3)
    print('world')

# asyncio.run()运行最高层级的conroutine
asyncio.run(main())
# hello
# sleep 3 second
# world

#################
# 协程调用过程： 
# 调用协程时，会被注册到ioloop，返回coroutine对象
# 用ensure_future 封装为Future对象
# 提交给ioloop
import aiohttp
import asyncio
import time

# async 函数被调用后会创建一个coroutine
# 这时候该协程并不会立即运行，
# 需要通过 ensure_future 或 create_task 方法生成 Task 后才会被调度执行
async def mission(time):
    await asyncio.sleep(time) 

async def main():
    start_time = time.time()
    # asyncio.create_task()封装成task，函数用来并发运行作为 asyncio 任务 的多个协程
    tasks = [asyncio.create_task(mission(1)) for proxy in range(10000)]
    [await t for t in tasks]
    print(time.time() - start_time)

if __name__ == "__main__":
    asyncio.run(main())




#########################
import asyncio
import time

async def coroutine_child1_demo():
    await asyncio.sleep(2)
    return 1
async def coroutine_child2_demo():
    await asyncio.sleep(5)
    return 2

tasks = [
    coroutine_child1_demo(),
    coroutine_child2_demo()
]

if __name__ == "__main__":
    start = time.time()  # 开始时间

    ioloop = asyncio.get_event_loop()  # 创建事件循环ioloop
    coroutine = asyncio.wait(tasks) # 启动协程
    # Future 是一种特殊的 低层级 可等待对象，表示一个异步操作的 最终结果
    future = asyncio.ensure_future(coroutine)   # 封装成一个future对象
    ioloop.run_until_complete(future) # 提交给ioloop,等future对象完成
    ioloop.close()   # 不进行ioloop读写要关闭

    #debug
    print(future.done())    # 协程任务是否完成
    print(future.result())  # 协程任务执行的结果

    end = time.time()  # 结束时间

    print(str(end-start))

# 建议阅读官方文档
# https://docs.python.org/zh-cn/3/library/asyncio-task.html
