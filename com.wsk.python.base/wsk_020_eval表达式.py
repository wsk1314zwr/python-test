"""
1. 一定不要直接使用eval运行 input输入的内容
2. system 用于执行cmd命令，成功返回0，失败返回错误信息
"""

print(eval("2+3+6+7"))

__import__("os").system("ls")   #  如果这个字符串是由input 输入并eval直接运行，会导致调用方可直接操作系统

cmd = input("请输入要计算的表达式：")
eval(cmd)  # 错误的写法，有很大的安全风险

