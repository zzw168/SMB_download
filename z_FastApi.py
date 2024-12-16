from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()


# 定义数据模型
class Record(BaseModel):
    id: int
    name: str
    age: int
    email: str
    avatar: Optional[str] = None


# 模拟数据库
records = [
    Record(id=1, name="张三", age=28, email="zhangsan@example.com", avatar="/images/1.png"),
    Record(id=2, name="李四", age=32, email="lisi@example.com", avatar="/images/9.png"),
]


# 获取所有记录
@app.get("/api/records", response_model=List[Record])
async def get_records():
    return records


# 根据 ID 获取记录
@app.get("/api/records/{record_id}", response_model=Record)
async def get_record(record_id: int):
    for record in records:
        if record.id == record_id:
            return record
    raise HTTPException(status_code=404, detail="Record not found")


# 添加新记录
@app.post("/api/records", response_model=Record, status_code=201)
async def add_record(record: Record):
    if any(r.id == record.id for r in records):
        raise HTTPException(status_code=400, detail="Record with this ID already exists")
    records.append(record)
    return record


# 更新记录
@app.put("/api/records", response_model=Record)
async def update_record(record: Record):
    for index, existing_record in enumerate(records):
        if existing_record.id == record.id:
            records[index] = record
            return record
    raise HTTPException(status_code=404, detail="Record not found")


# 删除记录
@app.delete("/api/records/{record_id}", response_model=dict)
async def delete_record(record_id: int):
    global records
    filtered_records = [record for record in records if record.id != record_id]
    if len(filtered_records) == len(records):
        raise HTTPException(status_code=404, detail="Record not found")
    records = filtered_records
    return {"message": "Record deleted successfully"}


# 启动服务（在调试模式下运行）
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8086)
