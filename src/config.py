from pydantic_settings import BaseSettings, SettingsConfigDict


class CommonSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="../.env.backend",
        extra="allow"
    )

class CelerySettings(CommonSettings):
    celery_app_name: str
    celery_broker_url: str
    celery_backend_url: str

class DataBaseSettings(CommonSettings):
    database_url: str
    database_echo: bool

class Settings:
    database_settings: DataBaseSettings = DataBaseSettings()

settings = Settings()