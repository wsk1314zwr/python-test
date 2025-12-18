#!/usr/bin/env python3
"""
冒烟测试脚本
"""
from pprint import pprint

from servyou_bitable.sdk.client import BitableClient
from servyou_bitable.sdk.model import QueryRecordParam, QueryRecordCondition, UpsertRecordsParam, CreateRecordBody

bitable_server_local = "http://127.0.0.1:8080/bitable"
# bitable_server_dev = "http://bitable-front.bitable-dev.devops.91lyd.com/bitable"
# bitable_server_test = "http://bitable-front.bitable-test.sit.91lyd.com/bitable"
# bitable_server_release = "http://bitable.servyou-release.devops.91lyd.com/bitable"
# bitable_server_prod = "https://formforge.17win.com/bitable"

app_id = "bitable-collect"

client = BitableClient(bitable_server_local, app_id)


def test_query() -> None:
    # 1. 构造参数
    param = QueryRecordParam(
        base_id="appvfzEuWsubV",
        table_id="tvvTycVXgvv",
        selectFieldIds=["f42jly257guti"],
        condition=QueryRecordCondition(
            logicOp="and",
            childrenConditions=[
                QueryRecordCondition(
                    logicOp="or",
                    childrenConditions=[
                        QueryRecordCondition(
                            fieldId="f42jly257guti",
                            compareOp="greater",
                            value=[1]
                        ),
                        QueryRecordCondition(
                            fieldId="f42jly257guti",
                            compareOp="less",
                            value=[0]
                        )
                    ]
                ),
                QueryRecordCondition(
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
            records = client.query_record(param)
            if not records:  # 空列表就停
                break
            print(f"第 {page_no} 页，返回条数：{len(records)}")
            pprint(records)
            page_no += 1

    except Exception as e:
        print("❌ 调用失败：", e)
        raise


def test_upsert() -> None:
    # 1. 构造参数
    param = UpsertRecordsParam(
        base_id="appvfzEuWsubV",
        table_id="tvvTycVXgvv",
        firstBatch=True,
        lastBatch=True,
        records=[
            CreateRecordBody(fields={"f42jly257guti": 8800888, "id": "我来自于北京111"}),  # 未指定 rowId 则是插入
            CreateRecordBody(rowId="rec_xxx", fields={"f42jly257guti": 990099, "id": "我来自于上海222"})  # 指定 rowId 即更新
        ]
    )
    # 2. 调用
    try:
        resp = client.upsert_records(param)
        print("upsert数据全部成功")

    except Exception as e:
        print("异常：", e)


# 仅在“python -m bitable_sdk.test_run”时执行
if __name__ == "__main__":
    print("---------------查询测试--------------")
    test_query()
    print()
    print("---------------upsert测试--------------")
    test_upsert()
