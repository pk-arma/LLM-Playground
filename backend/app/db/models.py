from sqlalchemy import Column, Integer, Text, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PromptHistory(Base):
    __tablename__ = 'prompt_history'

    id = Column(Integer, primary_key=True, index=True)
    prompt = Column(Text, nullable=False)
    response = Column(Text, nullable=False)
    temperature = Column(Float, nullable=False)