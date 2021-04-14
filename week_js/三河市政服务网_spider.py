import re
import time
import random
import requests
import json
import csv




target_urls = "http://zwfw.san-he.gov.cn/icity/icity/guestbook/interact#"



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36 Edg/80.0.361.111'
}

"""
如果在headers里面有set_cookies
那这个cookies就和首页有cookies是一样的
获取cookies就是向首页发起请求。然后获取cookies"""
response = requests.get(target_urls, headers=headers)
# 需要获取cookies才能爬取数据
# print(response.cookies['ICITYSession'])
# print(response.text)
res = response.text
# print(res)
# 获取sig值，在首页，用正则取出，在__signature中
text_re = "__signature = \"(.*)\""
match_obj = re.search(text_re, res)
# 这就是url后面的s=d134791608286542429        &t=3369_d49249_1608286575000
sig = match_obj.group(1)
print("这是sig值：", sig)


# 现在我们根据下面的js语句要用python来伪造key和t

# sig = "b580221608303975662"
key = ""
keyindex = -1
chars = "0123456789abcdef"
for i in range(0, 6):
    c = sig[keyindex + 1]
    key += c
    keyindex = chars.index(c)
    if keyindex < 0 and keyindex >= len(sig):
        keyindex = i
print("这是key值：", key)



# 现在来伪造下面的t
t = str(int(random.randint(999, 10000))) + "_" + key + "_" + str(int(time.time()))+"000"
ts = t.replace("+", "_")
# 这就是url后面的t=3369_d49249_1608286575000
print("这是t值", ts)





def requests_sha():

    for page in range(0, 43, 7):
        start_url = "http://zwfw.san-he.gov.cn/icity/api-v2/app.icity.guestbook.WriteCmd/getList?s={0}&t={1}".format(sig, ts)
        # print(start_url)
        data = {
            "start": page,
            "limit": 7,
            "TYPE@=": "2",
            "OPEN@=": "1"
        }
        response = requests.post(url=start_url, headers=headers, json=data)
        # print(response.text)
        # print(response.json())
        da = response.json()
        # da = json.loads(datas)
        print(">>>>>>正在从第{}条开始获取数据>>>>>>>>>".format(page))
        for i in range(0, 7):
            # TITLE/CONTENT
            title = da["data"][i]['TITLE']
            # print(da["data"][i]['TITLE'])
            content = da["data"][i]['CONTENT']
            # print(da["data"][i]['CONTENT'])
            # print("="*40)
            with open("三河市政服务网.csv", mode="a", encoding="utf-8", newline="") as f:
                # 传入一个文件对象f
                # 用csv_writer一个变量去接收一个csv的一个对象f
                csv_writer = csv.writer(f)
                # writerow()是以 一行一行的定入数据
                # 写入数据要有一个容器，写入哪些由自己决定
                csv_writer.writerow([title, content])
        # print("*"*50)



requests_sha()


















