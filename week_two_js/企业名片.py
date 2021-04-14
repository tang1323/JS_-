"""像这种的js逆向，在js里一定要经过JSON.parse函数的，这过程要经过几个函数
再得经过JSON.parse解密，所以要通过JSON.parse这个函数去调用其他的js加密函数
"""
import execjs
import json
import requests


def request():
    url = "https://vipapi.qimingpian.com/DataList/productListVip"
    headers = {
        'Accept': 'application / json, text / plain, * / *',
        'Content - Type': 'application / x - www - form - urlencoded',
        'Origin': 'https: // www.qimingpian.cn',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
    }
    # form_data = 'time_interval=&tag=&tag_type=&province=&lunci=&page=2&num=20&unionid='
    form_data = 'time_interval=&tag=&tag_type=and&province=&lunci=&page=2&num=20&unionid=hKzxcoUpbCPsChKk1tqJ12L0BTeHeBmA1DrlbAfG4WIBqPmokuv7liP7e3%2FsQN%2BseJWqqIs6kiQsM8IbOYgM5A%3D%3D'
    response = requests.post(url, headers=headers, data=form_data)

    # print(response.json())

    data = response.json()["encrypt_data"]
    return data


# print(request())
# encrypt_data = request()
def decrypt_data():

    with open("qi.js", 'r', encoding='utf8') as f:
        jscode = f.read()

    data = request()
    # 用execjs模块, 'o'是传入这个函数名，data是o这个函数的参数
    result = execjs.compile(jscode).call('o', data)
    # res = result.content.decode("utf-8")
    print(json.loads(result))


decrypt_data()





