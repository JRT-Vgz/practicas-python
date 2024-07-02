
from fastapi import APIRouter

router = APIRouter(prefix="/products", 
                   responses = {404: {"message": "No encontrado"}},
                   tags = ["products"])


products_list = ["Producto 1", "Producto 2", "Producto 3", "Producto 4"]


@router.get("/")
async def get_all_products():
    return products_list


@router.get("/{id}")
async def get_product_by_id(id: int):
    return products_list[id]