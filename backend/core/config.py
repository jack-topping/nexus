from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    app_name: str = "Nexus"
    environment: str = "development"

    anthropic_api_key: str
    tavily_api_key: str

    database_url: str

    # Comma-separated list of allowed origins, e.g. "http://localhost:5173,https://nexus.example.com"
    cors_origins: list[str] = ["http://localhost:5173"]

    # Swap to "claude-sonnet-4-5" (or later) for production
    claude_model: str = "claude-haiku-4-5-20251001"


settings = Settings()