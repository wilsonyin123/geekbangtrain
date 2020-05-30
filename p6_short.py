from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
   
    browser.get('https://movie.douban.com/subject/1292052/')
    time.sleep(1)


    btm1 = browser.find_element_by_xpath('//*[@id="hot-comments"]/a')
    btm1.click()
    time.sleep(10)
    print(browser.page_source)

except Exception as e:
    print(e)
# finally:    
#     browser.close()
    