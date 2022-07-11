from fastapi import FastAPI
import redis
import pandas as pd
# import asyncio

# import aioredis

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    global r
    r = redis.Redis(
        host="demo1-redis.redis.cache.windows.net",
        port="6379",
        password="L9c5g7iyu9iLreYHQr2nQGXpi7tVhEixoAzCaAg5qVA=",
    )

@app.post("/get_cache")
async def root():
    start_time = pd.Timestamp.now()
    value_ = r.hget('key1', 'value1')
    print(f"Time taken for preprocessing: {pd.Timestamp.now() - start_time}")
    return {"message": value_.decode()}