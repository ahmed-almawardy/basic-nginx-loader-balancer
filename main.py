from fastapi import FastAPI
import platform
app = FastAPI()


@app.get("/")
async def root():

    return {"message": f"Hello World from {platform.node()}"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
