from fastapi import FastAPI
import redis
import pandas as pd
# import asyncio
# import aioredis

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    try:
        global r
        r = redis.Redis(
            host="demo1redis.redis.cache.windows.net",
            port="6379",
            password="uQZ4WmnYA3CjhXXi3DtrnH1m0CHbGgqQDAzCaNPayYM=",
        )
    except:
        pass

@app.get("/get_cache")
async def root():
    start_time = pd.Timestamp.now()
    try:
        value_ = r.hget('key1', 'value1')
    except:
        value_ = str(start_time).encode()
        
    print(f"Time taken for preprocessing: {pd.Timestamp.now() - start_time}")
    return {"message": value_.decode()}
