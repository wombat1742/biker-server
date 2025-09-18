from fastapi import APIRouter


router = APIRouter()

@router.get("/welcome")
def welcome():
    return "welcome"