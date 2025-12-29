from fastapi import APIRouter, Depends
from app.db.session import SessionLocal
from app.db.models import PromptHistory
from app.core.model_leader import generate_text


router = APIRouter()

@router.post("/generate/")
def  generate(payload:dict):
    db = SessionLocal()
    response = generate_text(
        payload["prompt"],
        payload['max_tokens'],
        payload['temperature']
    )
    record = PromptHistory(
        prompt=payload["prompt"],
        response=response,
        temperature=payload['temperature']
    )
    db.add(record)
    db.commit()
    return {"response": response}