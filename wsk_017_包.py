# coding=utf-8
"""
1. 包就是一个有多个模块文件组成的目录
2. 必须有个__init__文件 ,此文件申明了包中可提供出去的模块
3. import 包名 就可以将包下所有的模块导入
4. 发布模块包的步骤：第一步：构建setup文件 第二步：进入命令行，使用费python3 setup.py build 构建py包， 第三步：输入python3 setup.py sdist 打成一个压缩包其后缀是tar.gz
5. 安装模块包的步骤：第一步：解压：tar -zxvf package_test-1.0.0.tar.gz  第二步：安装：sudo python3 setup.py install  ,此时我们就将模块包安装机器的py环境了,
    如果安装了pip，直接使用：pip install package_test-1.0.0.tar.gz
6. 包的使用与卸载：使用：直接在本机ipython或者ide中导入安装的包，即可使用 ，卸载 ： 通过 包.__file__ 获取安装包路径，然后通过 sudo rm -rf 即可删除卸载
7. pip 是一个通用的包管理工具，安装卸载到py2和py3的命令： sudo pip | pip3 install |uninstall 包名。例如： sudo pip3 install ipython
8. whl包：已经编译的包，类似于exe文件；tar包：tar.gz包：源文件，压缩并打包在一起，还没有编译。环境充足，可以用targz包，但想要快速稳定好用，最好还是whl包
9. whl包打包命令：python setup.py check ；python setup.py sdist bdist_wheel || true 安装命令： pip install xxx.whl;
"""
import package_test

package_test.sent_message.send(1)
package_test.receive_message.receive()

""" 另一种打包方式：可方便同时打包出xxx..tar.gz  xxx.whl文件
参考：/Users/skwang/Documents/workspace/workspace4/project/work_project/python-bitable/安装部署
"""