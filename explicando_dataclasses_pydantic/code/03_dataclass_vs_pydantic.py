# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pydantic>=2.0.0",
# ]
# ///
"""
Comparação entre dataclasses e Pydantic
"""

# region code
from dataclasses import dataclass

from pydantic import BaseModel, Field


@dataclass
class UsuarioDataclass:
    nome: str
    idade: int = 18
    ...


class UsuarioPydantic(BaseModel):
    nome: str
    idade: int = Field(default=18, description="Idade do usuário")
    ...


# endregion code

print("=== DATACLASS ===")
# usuario_dc = UsuarioDataclass(nome="Maria", idade="não é um número")
usuario_dc = UsuarioDataclass(nome="Maria")
print(f"✓ Nome: {usuario_dc.nome}")
print(f"✓ Idade: {usuario_dc.idade} (tipo: {type(usuario_dc.idade)})")

# print("=== PYDANTIC ===")
# usuario_pyd = UsuarioPydantic(nome="Maria", idade="trinta")
# usuario_pyd = UsuarioPydantic(nome="Maria")
# usuario_pyd = UsuarioPydantic(nome="João", idade="30")
# print(f"✓ Nome: {usuario_pyd.nome}")
# print(f"✓ Idade: {usuario_pyd.idade} (tipo: {type(usuario_pyd.idade)})")
