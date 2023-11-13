from api.login import LoginApi
from api.course import CourseApi

class TestUpdateCourse:
    Token = None
    def setup(self):
        self.login_api = LoginApi()
        self.course_api = CourseApi()
        # 获取验证码
        uuid = self.login_api.get_verify_code().json().get('uuid')
        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": uuid
        }
        # 登录
        response = self.login_api.login(request_body=login_data)
        # 存登录成功Token
        TestUpdateCourse.Token = response.json().get('token')

    def teardown(self):
        pass

    # 修改课程成功
    def test01_update_success(self):
        update_data = {
            "id": 43058,
            "name": "learning_interface_test",
            "subject": "6",
            "price": 998,
            "applicablePerson": "2",
            "info": "zzh修改"
        }
        response = self.course_api.update_course(token=TestUpdateCourse.Token, request_body=update_data)
        print(response.json())
        assert 200 == response.status_code
        assert '成功' in response.text
        assert 200 == response.json().get('code')

    # 修改课程失败（用户未登录）
    def test02_update_fail(self):
        update_data = {
            "id": 43058,
            "name": "learning_interface_test",
            "subject": "6",
            "price": 998,
            "applicablePerson": "2",
            "info": "zzh修改"
        }
        response = self.course_api.update_course(token='xxx', request_body=update_data)
        print(response.json())
        assert 200 == response.status_code
        assert '认证失败' in response.text
        assert 401 == response.json().get('code')
