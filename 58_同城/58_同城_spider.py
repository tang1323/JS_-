
import requests
import re


headers = {
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "content-length": "651",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "cookie": '58home=gz; id58=c5/nfF/cJTpUr/jqDLFOAg==; city=gz; 58tj_uuid=ed3c6fe2-8345-4390-92fd-c52184f97d6f; als=0; wmda_uuid=6abcd0f262a0ca5ab7cccf0f32f5ca2c; wmda_new_uuid=1; xxzl_cid=5914cf3ab7dd44b394d08cbc5f8267da; xzuid=a55d7ed2-f3c9-410b-91a8-ee1dceec4a16; xxzl_deviceid=QzprzglTHu11L6QkRRDT0paGVgnh7WdervxDPyKKeeCHSvVA4b2PepzqvBor7dX%2B; sessionid=36bc8c5e-a83f-4bc0-982f-bd9e0e72e07d; param8616=0; param8716kop=1; wmda_visited_projects=%3B1731916484865%3B11187958619315%3B10104579731767; xxzl_smartid=a8573b46f813a3078416b576f65f5d67; new_uv=2; utm_source=; spm=; init_refer=; wmda_session_id_1731916484865=1608272306438-4ce11464-f6a7-24fb; wmda_session_id_10104579731767=1608272309707-113d8a34-d17f-d10d; wmda_session_id_11187958619315=1608272311266-907b3a81-7081-c383; new_session=0; www58com="UserID=76496274810641&UserName=zf3kawsgl"; 58cooper="userid=76496274810641&username=zf3kawsgl"; 58uname=zf3kawsgl; PPU=UID=76496274810641&UN=zf3kawsgl&TT=a52bc92bff1b004413bf2ec7bda17f73&PBODY=SyS7MuFR_g2hVmtUH3jiezeB1cO3XEIJPFRlvQrUZByHlRkLeTqDA2ntT8kpSfBBQ2QwIEAJfgMp3R7uXoUNN_FbJomyAbmf161o3cvf0L7gpLmhJfnJj-kQDG1kpYtF-ZFTxM3V5fQ3oEKWaPFJ-TICJp5d-xUneDwuYx1mEtQ&VER=1; jl_list_left_banner=4',
    "origin": "https://sz.58.com",
    "referer": "https://sz.58.com/searchjob/?pts=1608272639469",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36 Edg/80.0.361.111"
}
res = requests.get(url="https://sz.58.com/searchjob/", headers=headers).text()
result = re.search(r"base64,(.*?)\)", res, flags=re.S).group(1)
print(result)















