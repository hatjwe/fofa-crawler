import requests
from lxml import etree
import random
import time
import urllib
import base64

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
}

#这里的代理IP需要自己去爬取或者添加,不想用可以不用
# proxylist = [
#     {'HTTP': '112.84.54.35:9999'},
#     {'HTTP': '175.44.109.144:9999'},
#     {'HTTP': '125.108.119.23:9000'}
# ]

# proxy = random.choice(proxylist)

def loadpage(url,begin,end):
    for page in range(begin,end+1):
        print("正在爬取第"+str(page)+"页：")
        fullurl = url+"&page="+str(page)
        response = requests.get(fullurl,headers=headers).text
        html = etree.HTML(response)
        req = html.xpath('//span[@class="aSpan"]/a[@target="_blank"]/@href')
        result = '\n'.join(req)
        print(result)
        with open('1.txt', "a") as f:
            text = f.write(str(result)+"\n")
            print("----------------第"+str(page)+"页已完成爬取----------------"+'\n')


if __name__ == '__main__':
    q = input('请输入关键字,如 "app="xxx" && country="CN"：等等')
    begin = int(input("请输入开始页数 最小为1："))
    end = int(input("请输入结束页数 最大为5："))
    cookie = input("请输入你的Cookie：")
    # cookies = '_fofapro_ars_session='+cookie+';result_per_page=20'
    cookies = 'cookie' + ';result_per_page=20'
    headers['cookie'] = cookies

    url = "https://fofa.so/result?"
    key = urllib.parse.urlencode({"q":q})
    key2 = base64.b64encode(q.encode('utf-8')).decode("utf-8")

    url = url+key+"&qbase64="+key2
    print(url)
    loadpage(url,begin,end)
    time.sleep(5)
