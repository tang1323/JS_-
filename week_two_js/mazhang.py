import requests
import re


# 现在进入检查有ser-cookies这个参数，那我们就请求起始url获取一下cookie
# 这起始的url
# url = 'http://www.zjmazhang.gov.cn/hdjlpt/published?via=pc'

start_url = 'http://www.zjmazhang.gov.cn/hdjlpt/published?via=pc'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36 Edg/80.0.361.111',
}


# def get_ck():
"""动态获取它的session"""
res = requests.get(url=start_url, headers=headers)
# 这里把token和session也获取了,现在我们要session和token
# return res.cookies

cookies_token = res.cookies
print(cookies_token)
token = cookies_token['XSRF-TOKEN']
session = cookies_token['szxx_session']
# print(token, session)
# exit()
# return token, session


# def get_se():
"""动态获取它的session,有时候一些参数不是在js逆向中，像这个在网页html中"""
resp = requests.get(start_url).text
# 在网页源码中，用re取出来
# print(resp)
cs = re.search(r"var _CSRF = '(.*)';", resp).group(1)
# print(cs)
# return cs



# print(get_ck())
# print(get_se())
# exit()







url = 'http://www.zjmazhang.gov.cn/hdjlpt/letter/pubList'

form_data = {
    'offset': 0,
    "limit": 20,
    "site_id": '759010'
}
# 这个网站检测cookie与X-CSRF-TOKEN
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36 Edg/80.0.361.111',
    'Referer': 'http://www.zjmazhang.gov.cn/hdjlpt/published?via=pc',
    'Cookie': 'szxx_session=eyJpdiI6IlM5d09cL1I3b05iVWRUWWN6R1NpN0tRPT0iLCJ2YWx1ZSI6IitndGdLVjlnSThtZU9iYkpldlM4dW9OM3JvRVJcL3o1aVlFa2FadHlxc0Z1XC9Rc1Q1cTVWXC9Ta2ZWUWEyZ0NyZ3kiLCJtYWMiOiIwMjlkYzM0YWFkMzExMTZjZjcwZmZiZDc2N2E1OWQxZjA1ZGI2OTAzNzMyY2FjZWQ2ZjU1MTRkNTIxMmY3YWEzIn0%3D',
    'Host': 'www.zjmazhang.gov.cn',

    # 'X-CSRF-TOKEN': 'REPvj8GwIzTApfMDTFDGyeJ05ZnRXFWVzMFEiFP5',
    'X-CSRF-TOKEN': 'puSlYk0VocO66AEOaXZ7FcRmMIh8weCF1ePaCfBF'
}


response = requests.post(url=url, headers=headers, data=form_data)
print(response)
print(response.json())


















