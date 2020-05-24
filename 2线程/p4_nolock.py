import threading
import time
NUM = 0
def addone():
    global NUM
    NUM += 1
    time.sleep(1)  #  必须休眠，否则观察不到脏数据
    print(NUM)

for i in range(10):
    t = threading.Thread(target = addone)
    t.start()

print('main thread stop')
