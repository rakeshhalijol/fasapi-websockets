from fastapi import FastAPI,WebSocket
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {"message": "Hello World"}

@app.websocket("/ws")
async def ws_ep(ws:WebSocket):
    print("Accepting...")
    await ws.accept()
    print("Accepted...")