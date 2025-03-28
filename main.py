from fastapi import FastAPI
import random
app = FastAPI()

@app.get("/Hello World")
async def root():
    return {"message": "Hello World"}

@app.get("/testando")
@app.get("/teste1")
async def funcaoteste():
    return {"teste": True, "num_aleatorio": random.randint(1, 2000) }
    return {"teste": True, "num_aleatorio": random.randint(1, 2000) }
