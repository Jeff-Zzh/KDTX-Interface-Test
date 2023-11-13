from api.login import LoginApi
from api.course import CourseApi
from api.contract import ContractApi
import config

# 测试类
class TestBusinessContract:
    # 静态变量、类变量 实现 方法间传参
    Token = None

    # 前置处理
    def setup(self):
        # 实例化接口对象
        self.login_api = LoginApi()
        self.course_api = CourseApi()
        self.contract_api = ContractApi()

    # 后置处理
    def teardown(self):
        pass

    # 1.登录成功
    def test01_login_success(self):
        print("-"*10 + "in " + __name__ + "::test_login_success" + '-'*10) # __name__获取本模块全包名：script.test03_contract_business
        # 获取验证码
        res_v = self.login_api.get_verify_code()
        uuid = res_v.json().get("uuid")
        print(res_v.status_code)
        print(res_v.json())

        # 登录
        request_body = {
            "username": "admin",
            "password": "HM_2023_test",  # HM_2023_test admin123
            "code": "2",
            "uuid":uuid
        }
        res_l = self.login_api.login(request_body=request_body)
        TestBusinessContract.Token = res_l.json().get("token") # 从登录成功的resopnse中获得到token 保存到类变量中，方便其他方法使用
        print(res_l.status_code)
        print(res_l.json())

    # 2.课程添加成功
    def test02_add_course(self):
        request_body = {
            "name": "测试开发提升课01",
            "subject": "6",
            "price": 899,
            "applicablePerson": "2",
            "info": "测试开发提升课01"
        }
        response = self.course_api.add_course(token=TestBusinessContract.Token, request_body=request_body)
        print(response.json())

    # 3.上传合同成功
    def test03_upload_contract(self):
        # f = open(file="../data/test.pdf", mode="rb") # 二进制 读文件
        f = open(file=config.BASE_PATH + "/data/test.pdf", mode="rb") # 二进制 读文件
        response = self.contract_api.upload_contract(token=TestBusinessContract.Token, file=f)
        print(response.json())

    # 4.合同新增
    def test04_add_contract(self):
        request_body = {
            "name": "测试888",
            "phone": "13612341888",
            "contractNo": "HT20001101", # 合同编号-唯一
            "subject": "6",
            "courseId": 99,
            "channel": "0",
            "activityId": 77,
            "fileName": "../data/test.pdf"
        }
        response = self.contract_api.add_contract(token=TestBusinessContract.Token, request_body=request_body)
        print(response.json())