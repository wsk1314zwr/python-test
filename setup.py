from distutils.core import setup

setup(
    name='package_test',  # 被发布的包的名字
    version='1.0.0',  # 发布的版本
    py_modules=['package_test.receive_message',
                'package_test.sent_message'],  # 发布的模块
    author='wsk',
    author_email='18521093275@163.com',
    url='http://www.headfirstlabs.com',  # 项目的首页
    description='这是我的第一个发布安装文件'
)
