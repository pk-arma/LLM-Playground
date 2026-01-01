from pathlib import Path
from dotenv import load_dotenv

# load env first
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

from app.db.session import engine
from app.db.models import Base

def create_tables():
    Base.metadata.create_all(bind=engine)
    print("✅ Tables created")

if __name__ == "__main__":
    create_tables()
