from api.login import LoginApi
from api.course import CourseApi

class TestDeleteCourse:
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
        TestDeleteCourse.Token = response.json().get('token')

    def teardown(self):
        pass

   # 课程删除成功
    def test01_delete_success(self):
        # course被删过一次后就没有了，对应course_id将找不到对应course,可以先进行add course或从update_course接口返回值中找存在的课程
        response = self.course_api.delete_course(token=TestDeleteCourse.Token, course_id=43058)
        print(response.json())
        assert 200 == response.status_code
        assert '成功' in response.text
        assert 200 == response.json().get('code')

    # 课程删除失败（课程id不存在）
    def test02_delete_fail_id_not_exist(self):
        response = self.course_api.delete_course(token=TestDeleteCourse.Token, course_id=-1)
        print(response.json())
        assert 200 == response.status_code
        assert '失败' in response.text
        assert 500 == response.json().get('code')


    # 课程删除失败（用户未登录）
    def test03_delete_fail_user_not_login(self):
        response = self.course_api.delete_course(token='xxx', course_id=110)
        print(response.json())
        assert 200 == response.status_code
        assert '失败' in response.text
        assert 401 == response.json().get('code')