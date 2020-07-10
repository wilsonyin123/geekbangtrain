import requests
from lxml import etree
from queue import Queue
import threading
import json

class CrawlThread(threading.Thread):
    '''
    爬虫类
    '''
    def __init__(self,thread_id,queue):
        super().__init__() 
        self.thread_id = thread_id  
        self.queue = queue

    def run(self):
        '''
        重写run方法
        '''
        print(f'启动线程：{self.thread_id}')
        self.scheduler()
        print(f'结束线程：{self.thread_id}')

    # 模拟任务调度
    def scheduler(self):
        while True:
            if self.queue.empty(): #队列为空不处理
                break
            else:
                page = self.queue.get()
                print('下载线程为：',self.thread_id," 下载页面：",page)
                url = f'https://book.douban.com/top250?start={page*25}'
                headers = {
                    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
                }
                try:
                    # downloader 下载器
                    response = requests.get(url,headers=headers) 
                    dataQueue.put(response.text)
                except Exception as e:
                    print('下载出现异常',e)

class ParserThread(threading.Thread):
    '''
    页面内容分析
    '''
    def __init__(self,thread_id,queue,file):
        threading.Thread.__init__(self)      # 上面使用了super()
        self.thread_id = thread_id
        self.queue = queue
        self.file = file

    def run(self):
        print(f'启动线程：{self.thread_id}')
        while not flag:                      # 这里有什么优化思路？
            try:
                item = self.queue.get(False) # 参数为false时队列为空，抛出异常
                if not item:                 # 为什么要判断？
                    continue
                self.parse_data(item)
                self.queue.task_done() # get之后检测是否会阻塞
            except Exception as e:
                pass
        print(f'结束线程：{self.thread_id}')

    def parse_data(self,item):
        '''
        解析网页内容的函数
        :param item:
        :return:
        '''
        try:
            html = etree.HTML(item)
            books = html.xpath('//div[@class="pl2"]')
            for book in books:
                try:
                    title = book.xpath('./a/text()')
                    link = book.xpath('./a/@href')
                    response={
                        'title':title,
                        'link':link
                    } 
                    #解析方法和scrapy相同，再构造一个json
                    json.dump(response,fp=self.file,ensure_ascii=False) 
                except Exception as e:
                    print('book error', e)

        except Exception as e:
            print('page error',e)


dataQueue = Queue() # 存放解析数据的queue
flag = False

if __name__ == '__main__':
    # 将结果保存到一个json文件中
    output = open('book.json','a',encoding='utf-8') 

    # 任务队列，存放网页的队列
    pageQueue = Queue(20) 
    for page in range(0,11): 
        pageQueue.put(page) 
    
    # 爬虫线程
    crawl_threads = []
    crawl_name_list = ['crawl_1','crawl_2','crawl_3'] 
    for thread_id in crawl_name_list:
        thread = CrawlThread(thread_id,pageQueue)
        thread.start() 
        crawl_threads.append(thread)
    
    # 解析线程
    parse_thread = []
    parser_name_list = ['parse_1','parse_2','parse_3']
    for thread_id in parser_name_list: 
        thread = ParserThread(thread_id,dataQueue,output)
        thread.start() 
        parse_thread.append(thread)

    # 结束crawl线程
    for t in crawl_threads:
        t.join()
    
    # 结束parse线程
    flag = True
    for t in parse_thread:
        t.join() 

    output.close()
    print('退出主线程')
    

