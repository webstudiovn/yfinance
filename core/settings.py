from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding="utf-8")

    token_telegram_bot: str
    db_host: str
    db_port: int
    db_login: str
    db_pass: str
    db_name: str

dbconfigs = Settings()
