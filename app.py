from fastapi import FastAPI
from pydantic import BaseModel

# Initialize the FastAPI application
app = FastAPI()

@app.get("/")
def read_root():
    return {"message":"Welcome to FASTAPI!"}

@app.get("/items")
def get_items():
    return ["item1","item2","item2"]


@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "name": f"Item {item_id}"}

class Item(BaseModel):
    name: str
    price: float
    description: str | None = None

@app.post("/items")
def create_item(item: Item):
    return {"message":"Item created successfully!","item":item}


@app.post("/items/{item_id}")
def update_item(item_id: int,item:Item):
    return {"message":"Item updated sucessfully!","item_id":item_id,"updated_item":item}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message":"Item delete successfully!","item_id":item_id}

@app.get("/search")
def search_items(query: str | None, limit: int =10):
    return {"query":query,"limit":limit}

@app.get("/product/{product_id}")
def get_product(product_id:int):
    if product_id < 0:
        return {"error":"Invalid product ID"}
    return {"product_id": product_id, "name": f"Product {product_id}"}


from fastapi import Depends

def common_dependency():
    return {"user":"admin"}

@app.get("/secure-data")
def secure_data(dep: dict = Depends(common_dependency)):
    return {"data":"sensitive info","user":dep["user"]}
