from pprint import pprint
from typing import List

from servyou_bitable.sdk.client import BitableClient
from servyou_bitable.sdk.model import QueryRecordParam, QueryRecordResp, QueryCondition
# noinspection PyProtectedMember
from servyou_bitable.util.table_util import _set_global_context

"""
#如下是入参、出参对象模型：
@dataclass
class QueryCondition:                           # 查询数据-入参-查询条件
    logicOp: Optional[str] = None               # 逻辑操作符，可选值：and、or，用于组合 childrenConditions
    childrenConditions: Optional[List["QueryCondition"]] = None  # 组合条件，当 logicOp 有值不为空
    compareOp: Optional[str] = None             # 比较操作符，logicOp 无值时必填，可选值：equal、notEqual、greater、greaterEqual、less、lessEqual、empty、notEmpty、like、notLike、in、notIn
    fieldId: Optional[str] = None               # 字段 id，logicOp 无值时必填
    value: Optional[List[Any]] = None           # 字段值数组
    
@dataclass
class QueryRecordParam:                         # 查询数据-入参
    table_id: str                               # 查询的表 ID，必填
    selectFieldIds: Optional[List[str]] = None  # 返回的字段 ID 列表，选填，不传则返回所有字段
    condition: Optional[QueryCondition] = None  # 查询条件，选填
    pageNo: Optional[int] = None                # 页码，选填，不传或小于 1 时则为第一页
    pageSize: Optional[int] = None              # 每页数量，选填，不传或小于 1 时则不分页

@dataclass
class QueryRecordResp:                          # 查询数据-出参
    rowId: str                                  # 记录 Id
    fields: Dict[str, Any]                      # 字段值，key 是字段 Id，value 是字段值
"""
if __name__ == "__main__":
    bitable_server_local = "http://127.0.0.1:8080/bitable"
    _set_global_context(base_id="appvfzEuWsubV")
    _set_global_context(bitable_url=bitable_server_local)

    client = BitableClient()
    # 1. 构造参数
    param = QueryRecordParam(
        table_id="tvvTycVXgvv",
        condition=QueryCondition(
            fieldId="f42jly257guti",
            compareOp="equal",
            value=[0]
        )
    )
    # 2. 调用
    records: List[QueryRecordResp] = client.query_record(param)
    print(f"返回条数：{len(records)}")
    pprint(records)
