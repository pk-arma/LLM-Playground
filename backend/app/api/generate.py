# from fastapi import APIRouter, Depends
# from app.db.session import SessionLocal
# from app.db.models import PromptHistory
# from app.core.model_leader import generate_text


# router = APIRouter()

# @router.post("/generate/")
# def  generate(payload:dict):
#     print("payload",payload)
#     db = SessionLocal()
#     response = generate_text(
#         payload["prompt"],
#         payload['max_tokens'],
#         payload['temperature']
#     )
#     record = PromptHistory(
#         prompt=payload["prompt"],
#         response=response,
#         temperature=payload['temperature']
#     )
#     db.add(record)
#     db.commit()
#     return {"response": response}

from fastapi import APIRouter
from app.schemas.prompt import GenerateRequest
from app.core.model_leader import generate_text
from app.db.session import SessionLocal
from app.db.models import PromptHistory



router = APIRouter()

@router.post("/generate")   # ❗ NO trailing slash
def generate(payload: GenerateRequest):
    print("payload:", payload)

    db = SessionLocal()

    response = generate_text(
        payload.prompt,
        payload.max_tokens,
        payload.temperature
    )

    record = PromptHistory(
        prompt=payload.prompt,
        response=response,
        temperature=payload.temperature
    )

    db.add(record)
    db.commit()

    return {"response": response}
