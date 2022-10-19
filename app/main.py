import uvicorn
from fastapi import FastAPI

from .routers.predict import router as predict_router

app = FastAPI(
    title="Base Project Fast_API",
    version='0.0.1',
    # docs_url=None  # Desativar Swagger
)

app.include_router(predict_router)


@app.get("/")
def home():
    return {"health_check": "OK"}


if __name__ == '__main__':
    uvicorn.run("main:app", host='localhost', port=8000, reload=True)
