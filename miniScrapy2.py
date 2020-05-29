import asyncio

@asyncio.coroutine
def task():
    print('request')
    yield from asyncio.sleep(3)
    print('response')


scheduler = [task(), task(), task()]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(*scheduler))
loop.close()
