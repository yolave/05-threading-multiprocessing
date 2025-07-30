from pydantic import BaseSettings


class Settings(BaseSettings):
    project_name: str = "Clean API Example"


settings = Settings()
