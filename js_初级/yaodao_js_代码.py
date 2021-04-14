







import requests
import time
import random
from hashlib import md5


class YDSpider:

    def __init__(self):
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Connection": "keep-alive",
            "Content-Length": "240",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "OUTFOX_SEARCH_USER_ID=1536660523@10.108.160.19; JSESSIONID=aaaEA3DBCV2AsgD9u1Wzx; OUTFOX_SEARCH_USER_ID_NCOO=1765036762.3431666; ___rl__test__cookies=1608211693136",
            "Host": "fanyi.youdao.com",
            "Origin": "http://fanyi.youdao.com",
            "Referer": "http://fanyi.youdao.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36 Edg/80.0.361.111",
            "X-Requested-With": "XMLHttpRequest",
        }

    def get_salt_sign_lts(self, word):

        # lts就是时间戳, 有小数点，我们要取后3位， 所以要乘于1000
        lts = str(int(time.time() * 1000))

        # salt_str就是lts + 0到9的数字
        salt = str(random.randint(0, 9))

        # sign就是有道翻译官方的"fanyideskweb" + word + salt + "Tbh5E8=q6U3EXe+&L[4c@",转换成一个md5值
        # md5就是加密成一个32位的16进制数
        str1 = "fanyideskweb" + word + salt + "Tbh5E8=q6U3EXe+&L[4c@"
        # 下面是生成md5值
        md = md5()
        md.update(str1.encode())
        sign = md.hexdigest()
        return salt, sign, lts

    # 没有在__init__初始化的就要写上参数word, 如果己经有了在__init__初始化，那就不用再写了
    def attack_yd(self, word):

        # 1.先拿到salt, sign, lts
        salt, sign, lts = self.get_salt_sign_lts(word)

        # 2.定义form 表单数据为字典：data={}
        data = {
            "i": word,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": salt,
            "sign": sign,
            "lts": lts,
            "bv": "e2e13ead7a7fddc7999f4bb56cc8511c",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME",
        }

        # 3.直接悔关请求：requests.post(url, data=data, headers=headers)
        html = requests.post(url=self.url, data=data, headers=self.headers)
        # print(html.json())
        ht_json = html.json()
        result = ht_json["translateResult"][0][0]
        tgt = result['tgt']
        src = result['src']
        # 4.获取相应的内容
        print("{0}  >>>翻译为>>>  {1}".format(src, tgt))

    def main(self):
        while True:
            # 输入要翻译的内容
            word = input("请输入你要翻译的文本（中文或者英文）,退出请点击e: \n")
            if word == 'e':
                break
            self.attack_yd(word)


if __name__ == "__main__":
    spider = YDSpider()
    spider.main()






































