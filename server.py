gunicorn serverforapp3.wsgi
from fastapi import FastAPI

app = FastAPI()


@app.get("/endpoint/{string}")
async def read_item(string):
    return {"string": string}
