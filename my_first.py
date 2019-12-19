import random
import math
import time

import requests
import json

'''
//构建*号塔
row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(row-i-1):
        print(" ", end="")
    for j in range(0,2*i+1):
        print("*", end="")
    print()
'''

# 豆瓣爬虫spider
'''
# 定义请求url
url = "https://movie.douban.com/j/search_subjects"
url1 = "https://movie.baidu.com/j/search_subjects"
# 定义请求头
headers = {
    "User-Agent": ""
}
# 循环构建请求参数并且发送请求
for page_start in range(0, 100, 20):
    params = {
        "type": "movie",
        "tag": "热门",
        "sort": "recommend",
        "page_limit": "1000000000000",
       # "page_start": page_start
    }
    response = requests.get(
        url=url,
        headers=headers,
        params=params
    )
    # 方式一:直接转换json方法
    # results = response.json()
    # 方式二: 手动转换
    # 获取字节串
    content = response.content
    # 转换成字符串
    string = content.decode('utf-8')
    # 把字符串转成python数据类型
    results = json.loads(string)
    # 解析结果
    for i in results["subjects"]:
        print(i["title"], i["rate"])

'''
##水仙花数
'''
while True:
    num = int(input("input please:"))
    num_0 = int(num / 100)
    num_1 = int(num % 100 / 10)
    num_2 = int(num % 10)
    num_re = 0
    num_real = num
    print("num_0=%d num_1=%d num_2=%d" % (num_0, num_1, num_2))
    if (num_0 * num_0 * num_0 + num_1 * num_1 * num_1 + num_2 * num_2 * num_2) == num:
        print("%d是一个水仙花数！" % num)
    else:
        print("%d不是一个水仙花数" % num)
    while num > 0:
        num_re = num_re * 10 + num % 10
        num = num // 10
        ##if num == 0:
        ##错误示范
        ##    num_re = num_re * 10
    print("%d的反转数为：%d" % (num_real, num_re))
'''

# bilibili URL:https://api.vc.bilibili.com/board/v1/ranking/top?page_size=10&next_offset=51&tag=%E4%BB%8A%E6%97%A5%E7%83%AD%E9%97%A8&platform=pc
# bilibili URL:https://api.vc.bilibili.com/board/v1/ranking/top?page_size=10&next_offset=21&tag=%E4%BB%8A%E6%97%A5%E7%83%AD%E9%97%A8&platform=pc
# User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 Safari/537.36 Edg/79.0.309.43

"""
def get_json(url):
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 Safari/537.36 Edg/79.0.309.43'
    }

    params = {
        'page_size': 10,
        'next_offset': str(num),
        'tag': '今日热门',
        'platform': 'pc'
    }

    try:
        html = requests.get(url,params=params,headers=headers)
        return html.json()

    except BaseException:
        print('request error')
        pass

def download(url,path):
    start = time.time() # 开始时间
    size = 0
    headers = {
        'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }

    response = requests.get(url,headers=headers,stream=True) # stream属性必须带上
    chunk_size = 1024 # 每次下载的数据大小
    content_size = int(response.headers['content-length']) # 总大小
    if response.status_code == 200:
        print('[文件大小]:%0.2f MB' %(content_size / chunk_size / 1024)) # 换算单位
        with open(path,'wb') as file:
            for data in response.iter_content(chunk_size=chunk_size):
                file.write(data)
                size += len(data) # 已下载的文件大小


if __name__ == '__main__':
    for i in range(10):
        url = 'http://api.vc.bilibili.com/board/v1/ranking/top?'
        num = i * 10 + 1
        html = get_json(url)
        infos = html['data']['items']
        for info in infos:
            title = info['item']['description']  # 小视频的标题
            video_url = info['item']['video_playurl']  # 小视频的下载链接
            print(title)

            # 为了防止有些视频没有提供下载链接的情况
            try:
                download(video_url, path='%s.mp4' % title)
                print('成功下载一个!')

            except BaseException:
                print('凉凉,下载失败')
                pass

        time.sleep(int(format(random.randint(2, 8))))  # 设置随机等待时间


"""

"""
from random import randint


def roll_dice(n=2):
    
    #摇色子

    #:param n: 色子的个数
    #:return: n颗色子点数之和
    
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


def add(a=0, b=0, c=0):
    return a + b - c


# 如果没有指定参数那么使用默认值摇两颗色子
print(roll_dice())
# 摇三颗色子
print(roll_dice(3))
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
# 传递参数时可以不按照设定的顺序进行传递
print(add(c=50, a=100, b=200))


def add1(*args):
    total = 0
    for val in args:
        total += val
    return total


print(add1())
print(add1(1))
print(add1(1, 2))
print(add1(1, 2, 3))
print(add1(1, 3, 5, 7, 9))


#nihaowua spider，php to python
"""

"""
import requests
import random
from lxml import etree
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def get_random_ua():  # 随机UA
    ua = UserAgent()
    return ua.random


headers = {
    'User-Agent': get_random_ua()
}

url = 'https://www.nihaowua.com/'


def get_ip_list(url, headers):
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[1].text + ':' + tds[2].text)
    return ip_list


def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    return proxies


def get_proxies():  # 随机IP
    url = 'http://www.xicidaili.com/nn/'
    ip_list = get_ip_list(url, headers=headers)
    proxies = get_random_ip(ip_list)
    return proxies


def main_print():  # 直接打印输出程序
    count = 0
    while True:
        res = requests.get(url=url, headers=headers, proxies=get_proxies())
        res.encoding = 'utf-8'
        selector = etree.HTML(res.text)
        xpath_reg = "//section/div/*/text()"
        results = selector.xpath(xpath_reg)
        content = results[0]
        count += 1
        print('********正在爬取中，这是第{}次爬取********'.format(count))
        print(content)


def main_keep():  # 写入txt文本程序
    count = 0
    with open("NiHaoWu.txt", "a") as f:
        while True:
            res = requests.get(url=url, headers=headers, proxies=get_proxies())
            res.encoding = 'utf-8'
            selector = etree.HTML(res.text)
            xpath_reg = "//section/div/*/text()"
            results = selector.xpath(xpath_reg)
            content = results[0]
            f.write(content + '\n')
            count += 1
            print('********正在爬取中，这是第{}次爬取********'.format(count))


if __name__ == '__main__':
    main_print()

"""

# import sys
# import time
# import urllib
# import urllib3
# import requests
# import numpy as np
# from bs4 import BeautifulSoup
# from openpyxl import Workbook
# from random import randint

"""

# chromedriver_path = "D:\EdgeDownload\chromedriver_win32\chromedriver.exe"
# weibo_username = "oentems@sina.com"
# weibo_password = "paigu0719."

# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 定义一个taobao类
class taobao_infos:

    # 对象初始化
    def __init__(self):
        url = 'https://login.taobao.com/member/login.jhtml'
        self.url = url

        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})  # 不加载图片,加快访问速度
        options.add_experimental_option('excludeSwitches',
                                        ['enable-automation'])  # 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium

        self.browser = webdriver.Chrome(executable_path=chromedriver_path, options=options)
        self.wait = WebDriverWait(self.browser, 10)  # 超时时长为10s

    # 登录淘宝
    def login(self):
        # 打开网页
        self.browser.get(self.url)

        # 等待 密码登录选项 出现s
        password_login = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.qrcode-login > .login-links > .forget-pwd')))
        password_login.click()

        # 等待 微博登录选项 出现
        weibo_login = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.weibo-login')))
        weibo_login.click()

        # 等待 微博账号 出现
        weibo_user = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.username > .W_input')))
        weibo_user.send_keys(weibo_username)

        # 等待 微博密码 出现
        weibo_pwd = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.password > .W_input')))
        weibo_pwd.send_keys(weibo_password)

        # 等待 登录按钮 出现
        submit = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btn_tip > a > span')))
        submit.click()

        # 直到获取到淘宝会员昵称才能确定是登录成功
        taobao_name = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                      '.site-nav-bd > ul.site-nav-bd-l > li#J_SiteNavLogin > div.site-nav-menu-hd > div.site-nav-user > a.site-nav-login-info-nick ')))
        # 输出淘宝昵称
        print(taobao_name.text)


# 使用教程：
# 1.下载chrome浏览器:https://www.google.com/chrome/
# 2.查看chrome浏览器的版本号，下载对应版本号的chromedriver驱动:http://chromedriver.storage.googleapis.com/index.html
# 3.填写chromedriver的绝对路径
# 4.执行命令pip install selenium
# 5.打开https://account.weibo.com/set/bindsns/bindtaobao并通过微博绑定淘宝账号密码

if __name__ == "__main__":
    chromedriver_path = "D:\EdgeDownload\chromedriver_win32\chromedriver.exe"  # 改成你的chromedriver的完整路径地址
    weibo_username = "onetems@sina.com"  # 改成你的微博账号
    weibo_password = "paigu0719."  # 改成你的微博密码

    a = taobao_infos()
    a.login()  # 登录
"""


def gcd(x, y):
    if x > y:
        x, y = y, x
    else:
        x, y = x, y
    for result in range(x, 0, -1):
        if x % result == 0 and y % result == 0:
            return result


def gcd_real(x, y):
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor


def __max(x, y):
    if x > y:
        x, y = y, x
    else:
        x, y = x, y
    for result in range(y, x * y + 1, 1):
        if result % x == 0 and result % y == 0:
            return result


num1 = int(input("please input the  first number:"))
num2 = int(input("please input the second number:"))
print(gcd(num1, num2), __max(num1, num2))
print(gcd_real(num1, num2))
