from fastapi import FastAPI

app = FastAPI()


@app.get("/endpoint/{string}")
async def read_item(string):
    return {"string": string}
