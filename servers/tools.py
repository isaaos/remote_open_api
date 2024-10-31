from fastapi import  Request, APIRouter

tools_app = APIRouter()

@tools_app.get("/get_ip")
async def get_ip(request: Request):
    try:
        client_ip = request.client.host  # 获取客户端 IP 地址
        return {"ip": client_ip}
    except Exception as e:
        return {"ip": '','msg':str(e)}