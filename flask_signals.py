from flask import Flask
from flask import signals

app = Flask(__name__)

def func1(*argv):
    print('func1')
    
# 在发起请求之前执行func1函数
signals.request_started.connect(func1)

@app.route('/')
def func():
    print('View Function')
    return "ok"

if __name__ == '__main__':
    app.run()