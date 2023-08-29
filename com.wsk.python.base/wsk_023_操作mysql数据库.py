import base64

import pymysql


# 测试环境的

def main():
    # connect

    pwd = base64.b64decode(b'eHhiWXVtYV9xc2xubjY2eHhi')
    pwd = bytes.decode(pwd)

    pwd = pwd[3:15]

    pwd = base64.b64decode(b'c2VydnlvdQ==')
    db = pymysql.connect(host='10.199.140.143', user='root', password=pwd, database='xxx', port=3306)
    cur = db.cursor()

    gl_sql = "select id from xxx.map_table_auth_apply where id > {}".format(700)
    cur.execute(gl_sql)
    data = cur.fetchall()
    print(data)
    cur.close()
    db.close()


if __name__ == '__main__':
    main()
