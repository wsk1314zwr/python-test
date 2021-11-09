import argparse

"""
命令行参数测试
"""
parser = argparse.ArgumentParser(description='hive  connection  argparse')
parser.add_argument('--host', '-host', help='host required=True', required=True)
parser.add_argument('--port', '-port', help='port default=10000', default=10000)
parser.add_argument('--username', '-username', help='username required=True', required=True)
parser.add_argument('--queue', '-queue', help='queue default=root.badmin', default='root.badmin')
args = parser.parse_args()
conf = {"hive.server2.proxy.user": args.username, "mapreduce.job.queuename": args.queue}
print(parser)
print(conf)
str2222 = """ ha ha ha  """
print(str2222)
