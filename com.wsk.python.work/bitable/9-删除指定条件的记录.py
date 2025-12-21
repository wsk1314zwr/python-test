
from servyou_bitable.sdk.client import BitableClient
from servyou_bitable.sdk.model import DeleteRecordParam, QueryCondition
# noinspection PyProtectedMember
from servyou_bitable.util.table_util import _set_global_context

"""
@dataclass
class QueryCondition:                           # 删除数据-入参-查询条件
    logicOp: Optional[str] = None               # 逻辑操作符，可选值：and、or，用于组合 childrenConditions
    childrenConditions: Optional[List["QueryCondition"]] = None  # 组合条件，当 logicOp 有值不为空
    compareOp: Optional[str] = None             # 比较操作符，logicOp 无值时必填，可选值：equal、notEqual、greater、greaterEqual、less、lessEqual、empty、notEmpty、like、notLike、in、notIn
    fieldId: Optional[str] = None               # 字段 id，logicOp 无值时必填
    value: Optional[List[Any]] = None           # 字段值数组

@dataclass
class DeleteRecordParam:                        # 删除数据-入参
    table_id: str                               # 表格 ID，必填
    rowIds: Optional[List[str]] = None          # 需要删除的数据的 rowId 集合，选填；若 rowIds、condition 都不填则删除表的所有数据
    condition: Optional[QueryCondition] = None  # 需要删除的数据的过滤条件，选填；若 rowIds、condition 都不填则删除表的所有数据
"""
if __name__ == "__main__":
    bitable_server_local = "http://127.0.0.1:8080/bitable"
    _set_global_context(base_id="appvfzEuWsubV")
    _set_global_context(bitable_url=bitable_server_local)
    client = BitableClient()
    # 1. 构造参数
    param = DeleteRecordParam(
        table_id="tvvTycVXgvv",
        condition=QueryCondition(
            fieldId="f42jly257guti",
            compareOp="equal",
            value=[8800888]
        )
    )
    # 2. 调用
    client.delete_records(param)
    print("删除成功")