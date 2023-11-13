from api.login import LoginApi
from api.course import CourseApi

class TestAddCourseApi:
    Token = None

    def setup(self):
        self.login_api = LoginApi()
        self.course_api = CourseApi()

        # 获取验证码
        res_v = self.login_api.get_verify_code()
        login_data = {
            "username":"admin",
            "password":"HM_2023_test",
            "code":"2",
            "uuid":res_v.json().get("uuid")
        }
        res_l = self.login_api.login(request_body=login_data)
        # 提取登陆成功的token
        TestAddCourseApi.Token = res_l.json().get('token')

    def teardown(self):
        pass

    # 课程添加成功
    def test01_success(self):
        add_data = {
            "name":"测试开发课01",
            "subject":"6",
            "price":899,
            "applicablePerson":"2"
        }
        response = self.course_api.add_course(token=TestAddCourseApi.Token,
                                              request_body=add_data)
        print(response.json())
        assert 200 == response.status_code
        assert '成功' in response.text
        assert 200 == response.json().get("code")

    # 课程添加失败(未登录)
    def test02_fail(self):
        add_data = {
            "name":"测试开发课02",
            "subject":"6",
            "price":899,
            "applicablePerson":"2"
        }
        response = self.course_api.add_course(token="xxx", # 没登录，所以没有token
                                              request_body=add_data)
        print(response.json())
        assert 200 == response.status_code
        assert '失败' in response.text
        assert 401 == response.json().get("code")
