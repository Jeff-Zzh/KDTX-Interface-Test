'''
    封装课程模块操作相关接口
    核心在于依据接口文档实现接口信息封装、重点关注接口如何被调用
'''
import requests

import config


# 创建接口类
class CourseApi:
    # 初始化
    def __init__(self):
        self.url_add_course = config.BASE_URL + "/api/clues/course" # 添加课程url
        self.url_select_course = config.BASE_URL + "/api/clues/course/list" # 查询课程url
        self.url_update_course = config.BASE_URL + "/api/clues/course"  # 修改课程url
        self.url_del_course = config.BASE_URL + "/api/clues/course"  # 删除课程url

    # 课程添加
    def add_course(self, token, request_body):
        return requests.post(url=self.url_add_course, headers={"Authorization":token}, json=request_body)
        # requests调用http对应请求时(get post put delete)如果形参有json=，那方法自己就会在请求头headers中加上键值对：Content-Type:applicaiton/json

    # 课程查询
    def select_course(self, params, token):
        return requests.get(url=self.url_select_course, params=params, headers={"Authorization":token})

    # 课程修改
    def update_course(self, token, request_body):
        return requests.put(url=self.url_update_course, headers={"Authorization":token}, json=request_body)

    # 课程删除
    def delete_course(self, token, course_id):
        return requests.delete(url=self.url_del_course + f'/{course_id}', headers={"Authorization":token})