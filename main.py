from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    """
    Endpoint de base qui retourne un message de bienvenue.
    """
    return {"message": "Bonjour de FastAPI! (via WSL/UV)"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    """
    Endpoint qui retourne un élément basé sur son ID.
    L'ID est automatiquement converti en entier (int).
    """
    return {"item_id": item_id, "description": "Ceci est un exemple d'élément."}