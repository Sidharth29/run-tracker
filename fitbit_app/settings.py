import os
from typing import List

from dotenv import find_dotenv, load_dotenv
from pydantic_settings import BaseSettings

load_dotenv(find_dotenv())


class Settings(BaseSettings):
    ACCESS_TOKEN: str = os.getenv("ACCESS_TOKEN", "")

    CLIENT_SECRET: str = os.getenv("CLIENT_SECRET", "")

    CLIENT_ID: str = os.getenv("CLIENT_ID", "")

    REFRESH_TOKEN: str = os.getenv("REFRESH_TOKEN", "")

    TOKEN_TYPE: str = os.getenv("TOKEN_TYPE", "Bearer")

    SCOPE: List = os.getenv(
        "SCOPE",
        [
            "sleep",
            "weight",
            "nutrition",
            "settings",
            "location",
            "heartrate",
            "activity",
            "social",
            "profile",
        ],
    )


def get_settings():
    return Settings()
