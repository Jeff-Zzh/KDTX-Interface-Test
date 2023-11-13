from api.login import LoginApi

# 测试类
class TestLoginApi:
    uuid = None

    # 前置处理
    def setup(self):
        # 实例化接口类
        self.login_api = LoginApi()
        # 获取验证码
        response = self.login_api.get_verify_code()
        # 提取uuid
        TestLoginApi.uuid = response.json().get("uuid")

    # 后置处理
    def teardown(self):
        pass

    # 登录成功
    def test01_success(self):
        login_data = {
            'username':'admin',
            'password':'HM_2023_test',
            'code':'2',
            'uuid':TestLoginApi.uuid
        }
        response = self.login_api.login(request_body=login_data)
        # 断言响应状态码为 200
        assert 200 == response.status_code
        # 断言响应数据包含'成功'
        assert '成功' in response.text
        # 断言响应code值为 200
        assert 200 == response.json().get('code')

    # 登录失败(用户名为空)
    def test02_login_without_username(self):
        login_data = {
            'username':'',
            'password':'HM_2023_test',
            'code':'2',
            'uuid':TestLoginApi.uuid
        }
        response = self.login_api.login(request_body=login_data)
        # 断言响应状态码为 200
        assert 200 == response.status_code
        # 断言响应数据包含'成功'
        assert '错误' in response.text
        # 断言响应code值为 200
        assert 500 == response.json().get('code')

    # 登录失败(未注册用户)
    def test03_username_not_exist(self):
        login_data = {
            'username':'not_exist',
            'password':'HM_2023_test',
            'code':'2',
            'uuid':TestLoginApi.uuid
        }
        response = self.login_api.login(request_body=login_data)
        # 断言响应状态码为 200
        assert 200 == response.status_code
        # 断言响应数据包含'成功'
        assert '错误' in response.text
        # 断言响应code值为 200
        assert 500 == response.json().get('code')