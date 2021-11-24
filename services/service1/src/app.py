from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {
        "msg": "Hello from Service 1"
    }