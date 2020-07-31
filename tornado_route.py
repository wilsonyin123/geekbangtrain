import tornado.ioloop
import tornado.web                              

class MainHandler(tornado.web.RequestHandler):  
    def get(self):                              
        self.write("Hello, world")
        # self.render("index.html")              

#路由映射
application = tornado.web.Application([         
    (r"/", MainHandler),                   
])

if __name__ == "__main__":
    application.listen(8000)                    
    tornado.ioloop.IOLoop.instance().start()

# gevent 代码好维护
# twisted 稳定性最好
# tornado 兼容性最好
