from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from sqlmodel import create_engine, Session

class DatabaseSettings(BaseSettings):
    connectionString: str = Field(alias="connectionString")
    sqlEcho: bool = Field(default=False)
    model_config = SettingsConfigDict(env_file=".env")
settings = DatabaseSettings()

engine = create_engine(settings.connectionString, echo=settings.sqlEcho)
DB = Session(engine)