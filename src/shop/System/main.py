from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Shop Management System API")

# គំរូទិន្នន័យសម្រាប់ទំនិញ (Product Schema)
class Product(BaseModel):
    id: int
    name: str
    price: float
    stock: int
    description: Optional[str] = None

# ទិន្នន័យបណ្តោះអាសន្ន (Mock Data)
products_db = []

# 1. API សម្រាប់មើលទំនិញទាំងអស់
@app.get("/products", response_model=List[Product])
def get_products():
    return products_db

# 2. API សម្រាប់បន្ថែមទំនិញថ្មី
@app.post("/products", response_model=Product)
def create_product(product: Product):
    for p in products_db:
        if p.id == product.id:
            raise HTTPException(status_code=400, detail="ID នេះមានរួចហើយ")
    products_db.append(product)
    return product

# 3. API សម្រាប់ស្វែងរកទំនិញតាម ID
@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    for product in products_db:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="រកមិនឃើញទំនិញឡើយ")
