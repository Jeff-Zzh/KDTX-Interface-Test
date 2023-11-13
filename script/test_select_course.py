from api.login import LoginApi
from api.course import CourseApi

# 测试类
class TestSelectCourse:
    Token = None

    def setup(self):
        self.login_api = LoginApi()
        self.course_api = CourseApi()
        # 获取验证码uuid
        res_v = self.login_api.get_verify_code()
        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": res_v.json().get('uuid')
        }
        # 登录
        res_l = self.login_api.login(request_body=login_data)
        # 获取登录成功的token
        TestSelectCourse.Token = res_l.json().get('token')

    def teardown(self):
        pass

    # 查询存在的课程
    def test01_select_success(self):
        response = self.course_api.select_course(params={'name':'测试开发提升课'}, token=TestSelectCourse.Token)
        print(response.json())
        assert 200 == response.status_code
        assert '成功' in response.text
        assert 200 == response.json().get('code')

    # 查询失败（用户未登录）
    def test02_select_fail(self):
        response = self.course_api.select_course(params={'subject':'6'}, token='xxx')
        print(response.json())
        assert 200 == response.status_code
        assert '认证失败' in response.text
        assert 401 == response.json().get('code')