from pathlib import Path
from dotenv import load_dotenv

# 👇 load env FIRST, before any other imports
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

# 🔽 now it's safe to import the rest
from fastapi import FastAPI
from app.api.generate import router

app = FastAPI()
app.include_router(router)
