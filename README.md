## 课达天下-接口测试自动化项目
根据黑马程序员视频构建 https://www.bilibili.com/video/BV1Cs4y1C73H/

- Python3用户 要安装pytest,requests,allure-pytest
```commandline
pip install pytest
```
```commandline
pip install requests
```
```commandline
pip install allure-pytest
```
- 接口自动化测试框架：pytest
- http请求发送：requests
- 测试报告：allure-pytest <br>
allure下载安装：https://github.com/allure-framework/allure2/releases <br>
本项目将allure-2.24.1.zip 放在 ./third-party路径下，下载解压后配置bin目录到系统环境变量<br>
然后在cmd `allure --version`查看到对应版本即说明安装成功
- 接口对象层调用requests包方法，关注**如何调用接口**根据接口API文档封装接口，接口响应结果返回给脚本层
- 测试脚本层关注**测试数据准备和断言、业务流程处理**，调用接口对象层发送请求，拿到接口对象层响应结果

### 项目执行
1. ./scripts中每个用例点进去，run --> 单条执行
2. 配置好`pytest.ini`，在pycharm终端 或 cmd/powershell等终端进入项目根目录执行`pytest`<br>
执行结果会直接显示在终端，同时，会产生对应的测试结果文件(.json)在配置的report报告目录中
> ========== 19 passed, 38 warnings in 216.10s (0:03:36) ==============
3. 使用allure:在终端输入`allure serve report`,就会启动本地的一个web服务，解析渲染<br>
`pytest`生成 的json测试结果文件
