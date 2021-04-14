
# JS逆向



urls = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'





# i: time
# from: AUTO
# to: AUTO
# smartresult: dict
# client: fanyideskweb
# salt: 16082117101167
# sign: 2775cff2726c1cf77b7064bf4d5af43e
# lts: 1608211710116
# bv: e2e13ead7a7fddc7999f4bb56cc8511c
# doctype: json
# version: 2.1
# keyfrom: fanyi.web
# action: FY_BY_REALTlME
#
#
#
#
# i: dog
# from: AUTO
# to: AUTO
# smartresult: dict
# client: fanyideskweb
#
# # 这三个字段不一样，那就是加密
# salt: 16082116931454
# sign: 30911f0b3c9f56592b948fc15348803c
# lts: 1608211693145
#
#
# bv: e2e13ead7a7fddc7999f4bb56cc8511c
# doctype: json
# version: 2.1
# keyfrom: fanyi.web
# action: FY_BY_REALTlME

"""
1.在Network里找到一个XHR文件，看一下里的form data信息，拿出来对比一下
2.比如拿一个form data里面的一个字段sign去sreach(搜索),输入sign,下面有一个js加密的文件，
	点击进入这个文件，会进入sources里面
3.在sources，有ctrl+f搜索一下sign的位置，逐一看过去有哪些是和form data是相似的
4.我们看到一个相似的东西，就用js的console.log()打印一下，比如打印console.log((new Date).getTime())

5.打印出来的(new Date).getTime()有点像我们python里的时间戳time.time()
那就知道了我们这个和时间戳一样，但是保留3位小数
phython的时间戳：1608213782.718834

js里面的(new Date).getTime()：1608213781261

这个就是我们的lts
那有一个salt: 16082117101167
这个相比：lts: 1608211710116
多了一个数字
就是这个js语句生成的parseInt(10 * Math.random(), 10)，从0-9随机生成一个的数字


sign:就是md5就是加密成一个32位的16进制数
"""
# import time
# print(time.time(), len(str(time.time())))



# md5就是加密成一个32位的16进制数
# str = "e2e13ead7a7fddc7999f4bb56cc8511c"
# print(len(str))


# 有一个包专门是用于密码学的
# from hashlib import md5
#
# str = "123456"
# md = md5()
# md.update(str.encode())     # 需要encode编码变成一个字符串
# res = md.hexdigest()
# print(res, len(res))

















