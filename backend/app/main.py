# from fastapi import FastAPI
# from app.api.generate import router

# app = FastAPI()
# app.include_router(router)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.generate import router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def root():
    return {"status": "LLM Playground API running"}

app.include_router(router)
