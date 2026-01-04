# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pydantic>=2.0.0",
#     "pydantic-settings>=2.0.0",
# ]
# ///
"""
Settings management com Pydantic
"""

# region code
import os

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    """
    Configurações da aplicação carregadas de variáveis de ambiente
    """

    app_name: str = Field(default="MeuApp", description="Nome da aplicação")
    debug: bool = Field(default=False, description="Modo debug")
    database_url: str = Field(description="URL de conexão do banco")
    database_pool_size: int = Field(default=10, ge=1, le=100)
    api_key: str = Field(description="Chave de API secreta")
    api_timeout: int = Field(default=30, gt=0)
    log_level: str = Field(default="INFO", pattern="^(DEBUG|INFO|WARNING|ERROR)$")

    model_config = SettingsConfigDict(
        env_file=".env",  # carrega de arquivo .env se existir
        env_file_encoding="utf-8",
        case_sensitive=False,  # DATABASE_URL = database_url
    )


# endregion code

os.environ["APP_NAME"] = "Sistema de Vendas"  # opcional
os.environ["DEBUG"] = "true"
os.environ["DATABASE_URL"] = "postgresql://user:pass@localhost/dbname"
os.environ["API_KEY"] = "secret-key-123"
os.environ["LOG_LEVEL"] = "DEBUG"
# os.environ["LOG_LEVEL"] = "INVALID"

# Carregar configurações
settings = AppSettings()

print("=== Configurações carregadas ===")
print(f"App: {settings.app_name}")
print(f"Debug: {settings.debug}")
print(f"Database: {settings.database_url}")
print(f"Pool size: {settings.database_pool_size}")
print(f"API key: {settings.api_key}")
print(f"API timeout: {settings.api_timeout}s")
print(f"Log level: {settings.log_level}")
