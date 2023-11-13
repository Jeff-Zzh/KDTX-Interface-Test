import requests

url = "http://kdtx-test.itheima.net/api/login"
request_header = {
    "Content-Type":"application/json"
}
request_body = {
    "username":"admin",
    "password":"HM_2023_test", # HM_2023_test admin123
    "code":"2",
    "uuid":"07f1d977c96d438c906ea680cacbebe3" #验证码接口返回uuid，每次都会变化
}
response = requests.post(url=url, headers=request_header, json=request_body)

print(response.status_code)
print(response.json())