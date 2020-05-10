from urllib import request

# GET 方法
resp = request.urlopen('http://httpbin.org/get')
print(resp.read().decode())

# POST 方法
resp = request.urlopen('http://httpbin.org/post', data=b'key=value', timeout=10)
print(resp.read().decode())

# cookie

from http import cookiejar
# 创建一个cookiejar对象
cookie = cookiejar.CookieJar()

# 创建cookie处理器
handler = request.HTTPCookieProcessor(cookie)

# 创建Opener对象
opener = request.build_opener(handler)

# 使用opener来发起请求
resp = opener.open('http://www.baidu.com')

# 查看之前的cookie对象，则可以看到访问百度获得的cookie
for i in cookie:
    print(i)

# 之后使用urlopen方法发起请求时，都会带上这个cookie
