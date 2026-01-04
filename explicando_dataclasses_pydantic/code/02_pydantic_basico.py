# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pydantic>=2.0.0",
# ]
# ///
"""
Exemplo básico de Pydantic: validação automática em runtime
"""

# region code
from pydantic import BaseModel


class Usuario(BaseModel):
    nome: str
    idade: int


usuario = Usuario(nome="Maria", idade=30)
# usuario = Usuario(nome="João")
# usuario = Usuario(nome="Ana", idade="trinta")
# usuario = Usuario(nome="Pedro", idade="25")
print(usuario)
# endregion code

# def processar_usuario(dados: Usuario) -> str:
#     nome = dados.nome
#     idade = dados.idade
#     if idade < 0:
#         raise ValueError("Idade não pode ser negativa")
#     return f"{nome} tem {idade} anos"

# def processar_usuario(dados: dict) -> str:
#     usuario = Usuario(**dados)
#     if usuario.idade < 0:
#         raise ValueError("Idade não pode ser negativa")
#     return f"{usuario.nome} tem {usuario.idade} anos"
