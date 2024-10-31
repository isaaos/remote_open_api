import multiprocessing
from fastapi import FastAPI
import uvicorn
from loguru import logger


from servers.tools import tools_app

app = FastAPI()

app.include_router(tools_app, prefix="/tools", tags=['小工具'])

def start_server():
    logger.info('API控制台: http://127.0.0.1:4040/redoc#tag/')
    logger.info('API展示台: http://127.0.0.1:4040/docs#/')
    # 获取 CPU 核心数量    reload=False 启用后不能使用workers
    cpu_count = multiprocessing.cpu_count()
    workers = cpu_count * 2 + 1  # 推荐的 workers 数量设置
    config = uvicorn.Config("servers.server:app", host="0.0.0.0", port=4040, workers=workers)
    server = uvicorn.Server(config)
    server.run()
