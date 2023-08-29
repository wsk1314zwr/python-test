import sys
import urllib3
import json
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    http = urllib3.PoolManager(num_pools=5, headers={'appCode': 'xxxworker'})
    resp = http.request('GET', 'http://xxx-manage-pc.xxx-release.devops.91lyd.com/xxx/api/meta/get-hive'
                               '-analyze-tables')
    data = json.loads(resp.data.decode('utf8'))
    resp.release_conn()
    status = data['head']['status']
    if status == 'Y':
        logger.info('========hive分析表开始处理========')
    else:
        logger.info('HTTP接口调用失败')
        sys.exit()

    sqlList = data['body']
    total = len(sqlList)
    it = iter(sqlList)
    index = 0
    error = 0
    for d in data['body']:
        print(d)

if __name__ == '__main__':
    main()
