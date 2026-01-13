
from pprint import pprint
from typing import List

from servyou_bitable.sdk.client import BitableClient
from servyou_bitable.sdk.model import QueryRecordParam, QueryRecordResp,UpsertRecordsParam, CreateRecordBody

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
    client = BitableClient()
    # 1. 构造查询参数
    param = QueryRecordParam(
        table_id=servyou_bitable._get_table_name('twkEAQzF7gN'),
        selectFieldIds=[servyou_bitable._get_field_name('twkEAQzF7gN', 'f8mx3k685z37'),servyou_bitable._get_field_name('twkEAQzF7gN', 'f0ujyw2s3hjq')]
    )
    # 2. 调用
    records: List[QueryRecordResp] = client.query_record(param)

    # 3. 过滤
    过滤records的元素的fields的key="f8mx3k685z37" 的value="销售出库"的数据，在第四步将的key="f0ujyw2s3hjq" 的value 赋值给 fp04w33v3z6g，然后在第四步按照 rowId过滤数据 

    # 4. 构造更新参数参数
    param = UpsertRecordsParam(
        table_id=servyou_bitable._get_table_name('twH3PXSq6fv'),
        records=[
            CreateRecordBody(rowId='第三步的rowId', fields={servyou_bitable._get_field_name('twkEAQzF7gN', 'fp04w33v3z6g'):'第三步的f0ujyw2s3hjq的值' })  # 指定 rowId 即更新
        ]
    )
    # 5. 调用
    client.upsert_records(param)
  




