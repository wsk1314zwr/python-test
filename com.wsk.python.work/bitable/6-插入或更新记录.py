from servyou_bitable.sdk.client import BitableClient
from servyou_bitable.sdk.model import UpsertRecordsParam, CreateRecordBody
# noinspection PyProtectedMember
from servyou_bitable.util.table_util import _set_global_context

"""
@dataclass
class CreateRecordBody:                         # 插入/更新数据-入参-单行内容
    fields: Dict[str, Any]                      # 字段值，key 是字段 Id，value 是字段值
    rowId: Optional[str] = None                 # 字段 rowId，指定则为更新，否则为新增

@dataclass
class UpsertRecordsParam:                       # 插入/更新数据-入参
    table_id: str                               # 查询的表 ID，必填
    records: List[CreateRecordBody]             # 单行内容列表，不为空
    firstBatch: bool = True                     # 是否是第一批数据，选填，默认 True；批量插入大量数据时，第一批插入 firstBatch 需为 True，lastBatch 需为 False
    lastBatch: bool = True                      # 是否是最后一批数据，选填，默认 True；批量插入大量数据时，最后一批插入 firstBatch 需为 False，lastBatch 需为 True
"""

if __name__ == "__main__":
    bitable_server_local = "http://127.0.0.1:8080/bitable"
    _set_global_context(base_id="appvfzEuWsubV")
    _set_global_context(bitable_url=bitable_server_local)

    client = BitableClient()
    # 1. 构造参数
    param = UpsertRecordsParam(
        table_id="tvvTycVXgvv",
        records=[
            CreateRecordBody(fields={"f42jly257guti": 88008, "id": "我来自于北京11"}),  # 未指定 rowId 则是插入
            CreateRecordBody(rowId="rec_xxx", fields={"f42jly257guti": 99008, "id": "我来自于上海22"})  # 指定 rowId 即更新
        ]
    )
    # 2. 调用
    client.upsert_records(param)
    print("upsert数据全部成功")


