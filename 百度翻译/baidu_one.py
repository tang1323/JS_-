

import requests
import execjs


class BaiduTranslateSpider:
    def __init__(self):
        self.url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

    def get_sign(self, word):
        """获取POST表单中sign的值"""
        # 使用test.js, 打开这个文件
        with open('test.js', 'r', encoding='utf8') as f:
            jscode = f.read()

        # 用execjs模块, 'e'是传入这个函数名，word是e这个函数的参数
        sign = execjs.compile(jscode).call('e', word)
        return sign

    def post_data(self, word, sign):

        # sign = self.get_sign(word)

        url = self.url
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
            'cookie': 'PSTM=1610799107; BAIDUID=2AF65C53BE34ED3CCF0DDCE28E8898D6:FG=1; H_PS_PSSID=; BIDUPSID=164C0BD7044388D7A1CDC5ABBA261EE9; delPer=0; PSINO=7; BA_HECTOR=80al2g848h04a50gud1g07sof0r; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BCLID=10219560016755668610; BDSFRCVID=y9IOJexroG3VEZTe0YCDbo12Z_weG7bTDYLEOwXPsp3LGJLVJeC6EG0Pts1-dEu-EHtdogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tR3aQ5rtKRTffjrnhPF32jFPXP6-hnjy3b7pKxcm5CJZEpbPhTLKWl4Wbttf5q3RymJ42-39LPO2hpRjyxv4y4Ldj4oxJpOJ-bCL0p5aHl51fbbvbURvD--g3-AqBM5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIE3-oJqC8-hI-l3J; BCLID_BFESS=10219560016755668610; BDSFRCVID_BFESS=y9IOJexroG3VEZTe0YCDbo12Z_weG7bTDYLEOwXPsp3LGJLVJeC6EG0Pts1-dEu-EHtdogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tR3aQ5rtKRTffjrnhPF32jFPXP6-hnjy3b7pKxcm5CJZEpbPhTLKWl4Wbttf5q3RymJ42-39LPO2hpRjyxv4y4Ldj4oxJpOJ-bCL0p5aHl51fbbvbURvD--g3-AqBM5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIE3-oJqC8-hI-l3J; __yjs_duid=1_1a90d67b283761996dddec925cabcba91610871575022; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; yjs_js_security_passport=594e051184b81bc65f0287d87cac34e47f03d61f_1610873954_js; ab_sr=1.0.0_MzM5NmNlMzkxODQ2ODA1NTIyZWM1MzExNGQxYmM5MTQ4OWE3YTI0ZTJkZmQ0MjVlOGMzZDVlOWNiZDdkZDQ1YzRjODYwZTBkNjI1NTc3NDdiYzY4MWI2OGFhMGQyZWU3; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1610871575,1610873952,1610873956; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1610873956; __yjsv5_shitong=1.0_7_b4871169225bb00086d0abf41d8985aca426_300_1610873956626_120.235.189.218_e8ab9c18'
        }

        formdata = {
            # 这个from是说英文翻译成to的中文，所以在这做了，中文翻译英文也可以
            "from": 'en' if word[0] in ['a', 'b', 'c', 'd', 'e', 'f', 'g' 'h', 'i',
                                        'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                                        's', 't', 'u', 'v', 'w', 's', 'y', 'z'] else "zh",
            'to': 'zh' or 'en',
            'query': word,
            'simple_means_flag': '3',
            'sign': sign,
            'token': '857fa8bef7ac376ced1e25571c92e5af',    # token是浏览器对象生成的，要用nodejs，但是在这里好像下写死的
            'domain': 'common',
        }

        response = requests.post(url, headers=headers, data=formdata)
        res = response.json()
        res_dst = res["trans_result"]['data'][0]
        res_src = res["trans_result"]['data'][0]
        src = res_src['src']   # 提问
        dst = res_dst['dst']   # 答案
        print("{0}  >>>翻译为>>>  {1}".format(src, dst))
        # print(response['trans_result']['data'][0]['dst'])
        # print(response.json())

    def run(self):
        while True:
            word = input("请输入你要翻译的文本（中文或者英文）,退出请点击e：")
            if word == 'e':
                break
            sign = self.get_sign(word)
            self.post_data(word, sign)




if __name__ == "__main__":
    baidu = BaiduTranslateSpider()
    baidu.run()












