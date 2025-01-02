from fastapi import APIRouter
from models.items import Item

router = APIRouter()

# Armazena itens em memória
items = []

@router.post("/items/")
def create_item(item: Item):
    items.append(item)
    return {"item": item}

@router.get("/items/")
def get_items():
    return {"items": items}

@router.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id < 0 or item_id >= len(items):
        return {"error": "Item não encontrado."}

    removed_item = items.pop(item_id)
    return {"message": "Item removido com sucesso.", "item": removed_item}
