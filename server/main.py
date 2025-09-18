from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .database.database import DatabaseSettings
from .routers import core, tests
app = FastAPI()


app.include_router(core.router)
app.include_router(tests.router)
app.mount("/", StaticFiles(directory="./server/public"), "public")


def main():
    pass


if __name__ == "__main__":
    main()
