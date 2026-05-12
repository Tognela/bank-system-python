from fastapi import FastAPI
from src.utils.api_routes import router
import uvicorn

app = FastAPI(
    title="Bank Tognela API",
    description="API REST do sistema bancario Bank Tognela",
    version="1.0.0"
)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)