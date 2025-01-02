from fastapi import FastAPI
from routers import items

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Registra as rotas de items
app.include_router(items.router)
