from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS 配置，允许前端访问后端
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源访问（生产环境建议指定具体来源）
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 定义数据模型
class Record(BaseModel):
    id: int
    name: str
    age: int
    email: str
    avatar: str = None  # 可选字段，默认值为 None

# 模拟数据库
records = [
    Record(id=1, name="张三", age=28, email="zhangsan@example.com", avatar="/images/1.png"),
    Record(id=2, name="李四", age=32, email="lisi@example.com", avatar="/images/9.png"),
]

# 获取所有记录
@app.get("/records", response_model=List[Record])
async def get_records():
    return records

# 新增记录
@app.post("/records", response_model=Record)
async def add_record(record: Record):
    # 检查 ID 是否重复
    if any(r.id == record.id for r in records):
        raise HTTPException(status_code=400, detail="记录 ID 已存在")
    records.append(record)
    return record

# 删除单条记录
@app.delete("/records/{record_id}", status_code=204)
async def delete_record(record_id: int):
    global records
    # 检查记录是否存在
    record = next((r for r in records if r.id == record_id), None)
    if not record:
        raise HTTPException(status_code=404, detail="记录未找到")
    records = [r for r in records if r.id != record_id]
    return

# 批量删除记录
@app.post("/records/batch-delete")
async def batch_delete_records(ids: List[int]):
    global records
    # 检查是否存在某些 ID 不在记录中
    not_found_ids = [id for id in ids if not any(r.id == id for r in records)]
    if not_found_ids:
        raise HTTPException(
            status_code=404, detail=f"以下记录未找到，无法删除: {not_found_ids}"
        )
    records = [r for r in records if r.id not in ids]
    return {"message": "批量删除成功", "deleted_ids": ids}

# 启动服务的入口
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8086)
