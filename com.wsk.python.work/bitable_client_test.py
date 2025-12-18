#!/usr/bin/env python3
"""
包内冒烟测试脚本，与 client.py 同层。
执行方式（项目根目录）：
    python -m bitable_sdk.test_run
"""
from pprint import pprint
from servyou_bitable.sdk.client import BitableClient
from servyou_bitable.sdk.model import QueryRecordParam, QueryRecordCondition


def main() -> None:
    # 1. 构造参数
    param = QueryRecordParam(
        app_id="bitable-collect",
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
        pageSize=1
    )

    url_base_local = "http://127.0.0.1:8080/bitable"
    url_base_dev = "http://bitable-front.bitable-dev.devops.91lyd.com/bitable"
    url_base_test = "http://bitable-front.bitable-test.sit.91lyd.com/bitable"
    url_base_release = "http://bitable.servyou-release.devops.91lyd.com/bitable"
    url_base_prod = "https://formforge.17win.com/bitable"
    # 2. 调用
    client = BitableClient(url_base_local)
    try:
        records = client.query_record(param)
        print("✅ 调用成功！返回条数：", len(records))
        pprint(records)

        param.pageNo=2
        records = client.query_record(param)
        print("✅ 调用成功！返回条数：", len(records))
        pprint(records)

    except Exception as e:
        print("❌ 调用失败：", e)
        raise


# 仅在“python -m bitable_sdk.test_run”时执行
if __name__ == "__main__":
    main()
