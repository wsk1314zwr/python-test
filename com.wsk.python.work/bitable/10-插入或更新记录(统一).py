from servyou_bitable.sdk.client import BitableClient
from servyou_bitable.sdk.model import CreateRecordBody
# noinspection PyProtectedMember
from servyou_bitable.util.table_util import _set_global_context

"""
@dataclass
class CreateRecordBody:                         # 插入/更新数据-入参-单行内容
    fields: Dict[str, Any]                      # 字段值，key 是字段 Id，value 是字段值
    rowId: Optional[str] = None                 # 字段 rowId，指定则为更新，否则为新增

"""

if __name__ == "__main__":
    bitable_server_local = "http://bitable-front.bitable-dev.devops.91lyd.com/bitable"
    _set_global_context(base_id="appvfzEuWsubV")
    _set_global_context(bitable_url=bitable_server_local)
    _set_global_context(operator_id="20250928001053710024010000094")

    client = BitableClient()
    # 1. 构造 CreateRecordBody 集合
    records = []
    for i in range(10):
        fields = {"f42jly257guti": 98000000 + i, "id": f"batch_upsert_{i}"}
        if i % 2 == 1:
            records.append(CreateRecordBody(fields=fields))  # 未指定 rowId 则是插入
        else:
            records.append(CreateRecordBody(rowId="rwh8rJUwgqw", fields=fields))  # 指定 rowId 即更新
    # 2. 调用
    client.batch_upsert_records(table_id="tvvTycVXgvv", records=records)
    print("batch_upsert_records 全部成功")
