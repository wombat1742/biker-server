from fastapi import APIRouter
from sqlmodel import select
from itertools import groupby


from ..database.database import DB
from ..models.Test import Test, TestBase, TestWithQuestionData
from ..models.Answer import AnswerBase

router = APIRouter()

@router.get("/api/tests/", response_model=TestBase)
def get_available_tests() -> list[Test]:
    return DB.exec(select(Test)).all()
@router.get("/api/test/{id}", response_model=TestWithQuestionData)
def get_test_by_id(id: int):
    return DB.get(Test, id)

@router.post("/api/bike_choice/")
def get_bike_choise_result(answers: dict[str, int]):
    answers =  dict((value, key) for key, value in answers.items() if key in ["mountain", "road", "hybrid", "folding"])
    return  {
        "result": answers[max(answers.keys())]
    }