from sqlmodel import SQLModel, Field, Relationship
from .Answer import Answer

class QuestionBase(SQLModel):
    id: int = Field(primary_key=True)
    text: str
    test_id: int
class Question(QuestionBase, table=True):
    test_id: int = Field(foreign_key="test.id")
    test: "Test" = Relationship(back_populates="questions")
    answers: list["Answer"] = Relationship(back_populates="question")

class QuestionWithData(QuestionBase):
    answers: list["Answer"] = []