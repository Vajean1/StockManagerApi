from fastapi import FastAPI
from database import init_db
from routes import categories, products, stockMovement

app = FastAPI(title="Stock Manager API")

@app.on_event("startup")
async def on_statup():
    init_db()

app.include_router(categories.router)
app.include_router(products.router)
app.include_router(stockMovement.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
