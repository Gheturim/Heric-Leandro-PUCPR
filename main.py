from fastapi import FastAPI

app = FastAPI()

@app.get("/Hello World")
async def root():
    return {"message": "Hello World"}

@app.get("/testando")
async def funcaoteste():
    return {"teste:" "deu certo"}
