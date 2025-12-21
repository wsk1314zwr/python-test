"""
demo
"""
from pprint import pprint

from typing import List
from servyou_bitable.sdk.client import BitableClient
from servyou_bitable.sdk.model import QueryRecordParam, QueryCondition, UpsertRecordsParam, CreateRecordBody, \
    QueryRecordResp
# noinspection PyProtectedMember
from servyou_bitable.util.table_util import _set_global_context


def test_query() -> None:
    # 1. 构造参数
    param = QueryRecordParam(
        table_id="tvvTycVXgvv",
        selectFieldIds=["f42jly257guti"],
        condition=QueryCondition(
            logicOp="and",
            childrenConditions=[
                QueryCondition(
                    logicOp="or",
                    childrenConditions=[
                        QueryCondition(
                            fieldId="f42jly257guti",
                            compareOp="greater",
                            value=[1]
                        ),
                        QueryCondition(
                            fieldId="f42jly257guti",
                            compareOp="less",
                            value=[0]
                        )
                    ]
                ),
                QueryCondition(
                    fieldId="f42jly257guti",
                    compareOp="notEmpty"
                )
            ]
        ),
        pageNo=1,
        pageSize=5
    )
    # 2. 调用
    try:
        page_no = 1
        while True:
            param.pageNo = page_no
            records: List[QueryRecordResp] = client.query_record(param)
            if not records:  # 空列表就停
                break
            print(f"第 {page_no} 页，返回条数：{len(records)}")
            pprint(records)
            page_no += 1

    except Exception as e:
        print("调用失败：", e)
        raise


def test_upsert() -> None:
    # 1. 构造参数
    param = UpsertRecordsParam(
        table_id="tvvTycVXgvv",
        firstBatch=True,
        lastBatch=True,
        records=[
            CreateRecordBody(fields={"f42jly257guti": 88008, "id": "我来自于北京11"}),  # 未指定 rowId 则是插入
            CreateRecordBody(rowId="rec_xxx", fields={"f42jly257guti": 99008, "id": "我来自于上海22"})  # 指定 rowId 即更新
        ]
    )
    # 2. 调用
    try:
        client.upsert_records(param)
        print("upsert数据全部成功")

    except Exception as e:
        print("异常：", e)


def test_delete() -> None:
    from servyou_bitable.sdk.model import DeleteRecordParam

    # 1. 按 rowId 删除示例
    param1 = DeleteRecordParam(
        table_id="tvvTycVXgvv",
        rowIds=["r05pm910pa1a"],
        condition=QueryCondition(
            fieldId="f42jly257guti",
            compareOp="equal",
            value=[8800888]
        )
    )
    try:
        client.delete_records(param1)
        print("删除成功")
    except Exception as e:
        print("删除异常：", e)


if __name__ == "__main__":
    bitable_server_local = "http://127.0.0.1:8080/bitable"
    # bitable_server_dev = "http://bitable-front.bitable-dev.devops.91lyd.com/bitable"
    # bitable_server_test = "http://bitable-front.bitable-test.sit.91lyd.com/bitable"
    # bitable_server_release = "http://bitable.servyou-release.devops.91lyd.com/bitable"
    # bitable_server_prod = "https://formforge.17win.com/bitable"

    _set_global_context(base_id="appvfzEuWsubV")
    _set_global_context(bitable_url=bitable_server_local)
    client = BitableClient()

    print("---------------查询测试--------------")
    test_query()
    print()
    print("---------------upsert测试--------------")
    test_upsert()
    print()
    print("---------------delete测试--------------")
    test_delete()
