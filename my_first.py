import random
import math
import requests
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
'''
import requests
import json

# 定义请求url
url = "https://movie.douban.com/j/search_subjects"
# 定义请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}
# 循环构建请求参数并且发送请求
for page_start in range(0, 100, 20):
    params = {
        "type": "movie",
        "tag": "热门",
        "sort": "recommend",
        "page_limit": "20",
        "page_start": page_start
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
    for movie in results["subjects"]:
        print(movie["title"], movie["rate"])
'''
##水仙花数

num = int(input("input please:"))
num_0 =int(num / 100)
num_1 = int(num % 100 / 10)
num_2 = int(num % 10)
print(num_0+" "+num_1+" "+num_2)
if((num_0 * num_0 * num_0 + num_1 * num_1 * num_1 + num_2 * num_2 * num_2) == num):
    print("这是一个水仙花数！")