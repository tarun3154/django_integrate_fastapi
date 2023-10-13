from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import requests

app = FastAPI()

# Model
class Item(BaseModel):
    title: str
    description: Optional[str] = None
    price: int

# Dummy database
items_db = []

# Function to fetch data from an external JSON API
def fetch_data_from_api():
    try:
        api_url = "https://dummyjson.com/products"
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            products = data.get("products", [])

            for product_data in products[:3]:  # Get the first three products
                item = Item(
                    title=product_data.get("title", ""),
                    description=product_data.get("description", None),
                    price=product_data.get("price", 0)
                )
                items_db.append(item)
        else:
            raise HTTPException(status_code=500, detail="Failed to fetch data from the API")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to process data from the API")

fetch_data_from_api()

# Create
@app.post("/items/", response_model=Item)
def create_item(item: Item):
    items_db.append(item)
    return item

# Read (All items)
@app.get("/items/", response_model=List[Item])
def read_items():
    return items_db

# Read (Single item)
@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    if 0 <= item_id < len(items_db):
        return items_db[item_id]
    raise HTTPException(status_code=404, detail="Item not found")

# Update
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    if 0 <= item_id < len(items_db):
        items_db[item_id] = item
        return item
    raise HTTPException(status_code=404, detail="Item not found")

# Delete
@app.delete("/items/{item_id}", response_model=Item)
def delete_item(item_id: int):
    if 0 <= item_id < len(items_db):
        deleted_item = items_db.pop(item_id)
        return deleted_item
    raise HTTPException(status_code=404, detail="Item not found")
