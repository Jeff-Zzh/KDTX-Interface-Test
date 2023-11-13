import requests


# 发送请求，得到响应
reponse = requests.get(url="http://kdtx-test.itheima.net/api/captchaImage")

print(reponse.status_code)
print(reponse.text)