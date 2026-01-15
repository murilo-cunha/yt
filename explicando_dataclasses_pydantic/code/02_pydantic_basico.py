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
