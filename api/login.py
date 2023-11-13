'''
    封装登录相关接口
    核心在于依据接口文档实现接口信息封装、重点关注接口如何被调用
'''
import requests

import config


# 创建接口类
class LoginApi:
    # 初始化
    def __init__(self):
        # 指定url
        self.url_verify = config.BASE_URL + "/api/captchaImage" # 获取验证码url
        self.url_login = config.BASE_URL + "/api/login" # 登录url

    # 获取验证码
    def get_verify_code(self):
        return requests.get(url=self.url_verify)

    # 登录
    def login(self, request_body):
        return requests.post(url=self.url_login, json=request_body)