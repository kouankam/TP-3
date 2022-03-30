from typing import Optional
from unittest import async_case
from fastapi import FastAPI
from shodan import Shodan
from colorama import init

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}
@app.get("/ip/{ip}")
async def get_ip(ip: str, key: Optional[str] = None):
    if key is None:
        return {"Error": "Please provide a valid API key"}
    else:
        try:
            api = Shodan(key)
            res = api.host(ip)
            return {
                "long": res["longitude"],
                "lat":res["latitude"],
            }
        except Exception as e:
            return {"Error": str(e)}
            
            