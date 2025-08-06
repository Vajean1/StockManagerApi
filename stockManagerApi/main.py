from fastapi import FastAPI
from database import init_db
from routes import categories

app = FastAPI(title="Stock Manager API")

def on_statup():
    init_db()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)

app.include_router(categories.router)
