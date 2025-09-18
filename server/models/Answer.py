from sqlmodel import SQLModel, Field, Relationship


class AnswerBase(SQLModel):
    key: str
    value: int
    text: str
class Answer(AnswerBase, table=True):
    id: int = Field(primary_key=True)
    question_id: int = Field(foreign_key="question.id")
    question: "Question" = Relationship(back_populates="answers")

