import requests
import lxml.etree
import csv
import time
import queue
import pandas as pd

# 禁断的魔术 短评


def download(request_url):
    # 请求头部信息
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    header = {}
    header['user-agent'] = user_agent
    response = requests.get(request_url, headers=header)

    # xml化处理
    selector = lxml.etree.HTML(response.text)

    # 短评得分
    star = selector.xpath('//*[@class="comment"]//span[2]/span[1]/@title')
    # 短评内容
    shorts = selector.xpath('//*[@class="comment-content"]/span/text()')
    # 有用
    vote = selector.xpath('//*[@class="comment"]//span[1]/span/text()')

    # 结尾页
    end = selector.xpath('//*[@class="comment-paginator"]/li[3]/span/@class')

    return zip(star, vote, shorts), end


def write_to_file(page_content, filename='book.csv'):
    with open(filename, "a", encoding='utf-8') as csvFile:
        writer = csv.writer(csvFile)
        for line in page_content:
            writer.writerow(line)


def write_to_queue(page_content, content_queue):
    for line in page_content:
        content_queue.put(line)



if __name__ == '__main__':
    book_shorts = []
    q = queue.Queue()
    for page in range(1, 31):
        url = f'https://book.douban.com/subject/30317421/comments/hot?p={page}'

        content, endpage = download(url)
        write_to_queue(content,q)
        write_to_file(content)
        if endpage:
            # print(f'debug --- {endpage}')
            if endpage[0] == 'page-disabled':
                break
        time.sleep(2)

    while  True:
        if not q.empty():
            book_shorts.append(q.get())
        else:
            break

    df = pd.DataFrame(book_shorts)