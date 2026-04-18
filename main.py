from fastapi import FastAPI

app = FastAPI()

items = []

@app.get("/")
def home():
    return {"message": "this is fastapi"}

@app.get("/status")
def status():
    return {"status": "running"}

@app.get("/items")
def get_items():
    return {"items": items}

@app.post("/items")
def add_item(item: str):
    items.append(item)
    return{"message": "item added","items": items}

