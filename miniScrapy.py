import requests
from lxml import etree
from queue import Queue
import threading
import json
'''
Queue.qsize(队列名) #返回队列的大小
Queue.empty(队列名) # 队列为空返回true，否则为false
Queue.full(队列名) # 队列满返回true
Queue.get(队列名,值) # 出队
Queue.put(队列名,值) # 入队
FIFO 先进先出
'''

class Crawl_thread(threading.Thread):
    '''
    抓取线程类，注意需要继承线程类Thread
    '''
    def __init__(self,thread_id,queue):
        threading.Thread.__init__(self) # 需要对父类的构造函数进行初始化
        self.thread_id = thread_id  
        self.queue = queue # 任务队列

    def run(self):
        '''
        线程在调用过程中就会调用对应的run方法
        :return:
        '''
        print('启动线程：',self.thread_id)
        self.crawl_spider()
        print('退出了该线程：',self.thread_id)

    def crawl_spider(self):
        while True:
            if self.queue.empty(): #如果队列为空，则跳出
                break
            else:
                page = self.queue.get()
                print('当前工作的线程为：',self.thread_id," 正在采集：",page)
                url = 'https://www.qiushibaike.com/Shr/page/{}/'.format(str(page))
                headers = {
                    'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3371.0 Safari/537.36'
                }
                try:
                    content = requests.get(url,headers=headers)
                    data_queue.put(content.text) # 将采集的结果放入data_queue中
                except Exception as e:
                    print('采集线程错误',e)

class Parser_thread(threading.Thread):
    '''
    解析网页的类，就是对采集结果进行解析，也是多线程方式进行解析
    '''
    def __init__(self,thread_id,queue,file):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.queue = queue
        self.file = file

    def run(self):
        print('启动线程：', self.thread_id)
        while not flag:
            try:
                item = self.queue.get(False) # get参数为false时队列为空，会抛出异常
                if not item:
                    pass
                self.parse_data(item)
                self.queue.task_done() # 每当发出一次get操作，就会提示是否堵塞
            except Exception as e:
                pass
        print('退出了该线程：', self.thread_id)
    def parse_data(self,item):
        '''
        解析网页内容的函数
        :param item:
        :return:
        '''
        try:
            html = etree.HTML(item)
            result = html.xpath('//div[contains(@id,"qiushi_tag")]') # 匹配所有段子内容
            for site in result:
                try:
                    img_url = site.xpath('.//img/@src')[0] # 糗事图片
                    title = site.xpath('.//h2')[0].text # 糗事题目
                    content = site.xpath('.//div[@class="content"]/span')[0].text.strip() # 糗事内容
                    response={
                        'img_url':img_url,
                        'title':title,
                        'content':content
                    } #构造json
                    json.dump(response,fp=self.file,ensure_ascii=False) # 存放json文件
                except Exception as e:
                    print('parse 2: ', e)

        except Exception as e:
            print('parse 1: ',e)


data_queue = Queue() # 存放解析数据的queue
flag = False
def main():
    output = open('qiushi.json','a',encoding='utf-8') # 将结果保存到一个json文件中
    pageQueue = Queue(50) # 任务队列，存放网页的队列
    for page in range(1,11): 
        pageQueue.put(page) # 构造任务队列
    # 初始化采集线程
    crawl_threads = []
    crawl_name_list = ['crawl_1','crawl_2','crawl_3'] # 总共构造3个爬虫线程
    for thread_id in crawl_name_list:
        thread = Crawl_thread(thread_id,pageQueue) # 启动爬虫线程
        thread.start() # 启动线程
        crawl_threads.append(thread)
    # 初始化解析线程
    parse_thread = []
    parser_name_list = ['parse_1','parse_2','parse_3']
    for thread_id in parser_name_list: # 
        thread = Parser_thread(thread_id,data_queue,output)
        thread.start() # 启动线程
        parse_thread.append(thread)

    # 等待队列情况，先进行网页的抓取
    while not pageQueue.empty(): # 判断是否为空
        pass # 不为空，则继续阻塞

    # 等待所有线程结束
    for t in crawl_threads:
        t.join()
    # 等待队列情况，对采集的页面队列中的页面进行解析，等待所有页面解析完成
    while not data_queue.empty():
        pass
    # 通知线程退出
    global flag
    flag = True
    for t in parse_thread:
        t.join() # 等待所有线程执行到此处再继续往下执行

    print('退出主线程')
    output.close()

if __name__ == '__main__':
    main()