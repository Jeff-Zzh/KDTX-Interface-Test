import config
from api.login import LoginApi
import pytest
import json

# 数据驱动-测试数据
# test_data = [
#     ('admin', 'HM_2023_test', 200, '成功', 200),
#     ('', 'HM_2023_test', 200, '错误', 500),
#     ('not_exist', 'HM_2023_test', 200, '错误', 500)
# ]

# 读取json文件
def build_data(json_file):
    test_data = []
    # 打开json文件
    with open(json_file, 'r', encoding='utf-8') as f:
        # 加载json文件数据
        json_data = json.load(f)
        # 循环遍历拿数据
        for case_data in json_data:
            username = case_data.get("username")
            password = case_data.get("password")
            status_code = case_data.get("status_code")
            message = case_data.get("message")
            code = case_data.get("code")
            # 转换数据格式[{},{}] -> [(),()]
            test_data.append((username,password,status_code,message,code))
    return test_data

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

    # 登录
    @pytest.mark.parametrize('username,password,status_code,message,code', build_data(json_file=config.BASE_PATH + "/data/login.json"))
    def test01_success(self, username, password, status_code, message, code):
        login_data = {
            'username': username,
            'password': password,
            'code': '2',
            'uuid': TestLoginApi.uuid
        }
        response = self.login_api.login(request_body=login_data)
        # 断言响应状态码为 200
        assert status_code == response.status_code
        # 断言响应数据包含'成功'
        assert message in response.text
        # 断言响应code值为 200
        assert code == response.json().get('code')

    # # 登录失败(用户名为空)
    # def test02_login_without_username(self):
    #     login_data = {
    #         'username': '',
    #         'password': 'HM_2023_test',
    #         'code': '2',
    #         'uuid': TestLoginApi.uuid
    #     }
    #     response = self.login_api.login(request_body=login_data)
    #     # 断言响应状态码为 200
    #     assert 200 == response.status_code
    #     # 断言响应数据包含'成功'
    #     assert '错误' in response.text
    #     # 断言响应code值为 200
    #     assert 500 == response.json().get('code')
    #
    # # 登录失败(未注册用户)
    # def test03_username_not_exist(self):
    #     login_data = {
    #         'username': 'not_exist',
    #         'password': 'HM_2023_test',
    #         'code': '2',
    #         'uuid': TestLoginApi.uuid
    #     }
    #     response = self.login_api.login(request_body=login_data)
    #     # 断言响应状态码为 200
    #     assert 200 == response.status_code
    #     # 断言响应数据包含'成功'
    #     assert '错误' in response.text
    #     # 断言响应code值为 200
    #     assert 500 == response.json().get('code')
