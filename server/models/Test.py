from sqlmodel import SQLModel, Field, Relationship
from .Question import QuestionWithData, Question
class TestBase(SQLModel):
    id: int
    name: str       
    title: str
class Test(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str = Field(index=True, unique=True)
    title: str
    post_action: str
    questions: list[Question] = Relationship(back_populates="test")
class TestWithQuestionData(TestBase):
    questions: list[QuestionWithData] = []
    post_action: str

