# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pydantic>=2.0.0",
# ]
# ///
"""
Serialização: conversão de/para dict e JSON
"""

# region code
import json
from datetime import date

from pydantic import BaseModel, Field


class Endereco(BaseModel):
    rua: str
    numero: int
    cidade: str


class Usuario(BaseModel):
    nome: str
    idade: int = Field(gt=0)
    email: str
    data_cadastro: date
    endereco: Endereco


# endregion code

# Exemplo 1: Criar objeto a partir de dict
dados_dict = {
    "nome": "Maria Silva",
    "idade": 30,
    "email": "maria@example.com",
    "data_cadastro": "2025-01-04",
    "endereco": {"rua": "Av. Paulista", "numero": 1000, "cidade": "São Paulo"},
}

usuario = Usuario(**dados_dict)
print("=== Objeto criado ===")
print(f"Nome: {usuario.nome}")
print(f"Email: {usuario.email}")

# # Exemplo 2: Exportar para dict
# usuario_dict = usuario.model_dump()
# print("\n=== Export para dict ===")
# print(usuario_dict)
# print(f"Tipo data_cadastro: {type(usuario_dict['data_cadastro'])}")

# # Exemplo 3: Exportar para JSON
# usuario_json = usuario.model_dump_json(indent=2)
# print("\n=== Export para JSON ===")
# print(usuario_json)

# # Exemplo 4: Criar a partir de JSON string
# json_string = """
# {
#     "nome": "João Santos",
#     "idade": 25,
#     "email": "joao@example.com",
#     "data_cadastro": "2025-01-03",
#     "endereco": {
#         "rua": "Rua das Flores",
#         "numero": 500,
#         "cidade": "Rio de Janeiro"
#     }
# }
# """

# usuario2 = Usuario.model_validate_json(json_string)
# print("\n=== Criado a partir de JSON ===")
# print(f"Nome: {usuario2.nome}")
# print(f"Idade: {usuario2.idade}")

# # Exemplo 5: Serialização customizada
# usuario_dict_custom = usuario.model_dump(
#     include={"nome", "email"},  # apenas esses campos
#     exclude_none=True,  # exclui valores None
# )
# print("\n=== Dict customizado (apenas nome e email) ===")
# print(usuario_dict_custom)

# # Exemplo 6: Mode='json' para tipos serializáveis
# usuario_dict_json_mode = usuario.model_dump(mode="json")
# print("\n=== Dict com mode='json' (data como string) ===")
# print(usuario_dict_json_mode)
# print(f"Tipo data_cadastro: {type(usuario_dict_json_mode['data_cadastro'])}")
