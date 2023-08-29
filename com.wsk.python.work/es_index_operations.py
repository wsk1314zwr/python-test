"""
生成新的索引，并绑定别名，并移除旧的索引
"""
import base64
import datetime

from elasticsearch import Elasticsearch


def conn_es(auth_name, auth_pw):
    es = Elasticsearch(
        ['10.199.151.14:9200'],
        http_auth=(auth_name, auth_pw)
    )

    return es


def create_indices(es, index_name, alias_name):
    if not es.indices.exists(index=index_name):
        print(es.indices.create(index=index_name))
    if not es.indices.exists_alias(name=alias_name, index=index_name):
        print(es.indices.put_alias(index=index_name, name=alias_name))


def delete_indices(es, index_name, alias_name):
    """
    移除旧的索引绑定关系
    """
    if es.indices.exists_alias(index='mysearch-dwd_usr_tax_collect_customer_info_df-*', name=alias_name):
        index_dict = es.indices.get_alias(index='mysearch-dwd_usr_tax_collect_customer_info_df-*', name=alias_name)
        for _index_name in index_dict:
            if not _index_name == index_name:
                print(es.indices.delete_alias(index=_index_name, name=alias_name))

def delete_old_index(day):
    """
    删除day天前的旧索引
    """
    all_index = es.indices.get(index="mysearch-dwd_usr_tax_collect_customer_info_df-*")
    for ind in all_index:
        date_str = ind[-8:]
        date = datetime.datetime.strptime(date_str, '%Y%m%d')
        now_date = datetime.datetime.strptime('2021-12-22', '%Y-%m-%d')
        if date.timestamp() + day * 24 * 60 * 60 < now_date.timestamp():
            es.indices.delete(index=ind)



if __name__ == '__main__':
    # 连接es
    h = base64.b64decode(b'bXlzZWFyY2g=').decode()
    auth_pw = base64.b64decode(b'bXlzZWFyY2hfMTIz').decode()
    es = conn_es(auth_name, auth_pw)

    # 索引名称
    now = datetime.datetime.strptime('2021-12-22', '%Y-%m-%d').date()
    index_name = 'mysearch-dwd_usr_tax_collect_customer_info_df-' + str(now.strftime('%Y%m%d'))
    alias_name = 'mysearch-dwd_usr_tax_collect_customer_info_df-alias'

    # 创建新索引
    create_indices(es, index_name, alias_name)

    # 删除索引别名
    delete_indices(es, index_name, alias_name)

    # 删除三天前的旧索引
    delete_old_index(3)
