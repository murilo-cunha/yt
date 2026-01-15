# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pydantic>=2.0.0",
# ]
# ///
"""
Field com metadata e constraints
"""

# region code
from pydantic import BaseModel, Field


class Usuario(BaseModel):
    nome: str = Field(
        min_length=2, max_length=50, description="Nome completo do usuário"
    )
    idade: int = Field(
        gt=0,  # greater than (>)
        lt=150,  # less than (<)
        description="Idade em anos",
    )
    email: str = Field(
        pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
        description="Email válido",
    )
    tags: list[str] = Field(
        min_length=1, max_length=5, description="Lista de tags (1-5 itens)"
    )


# endregion code

# Exemplos
usuario = Usuario(
    nome="Maria Silva", idade=30, email="maria@example.com", tags=["python", "pydantic"]
)
# usuario = Usuario(nome="A", idade=30, email="a@b.com", tags=["tag"])
# usuario = Usuario(nome="João", idade=0, email="joao@example.com", tags=["tag"])
# usuario = Usuario(nome="Pedro", idade=40, email="pedro.com", tags=["da", "um", "like", "no", "video", "pf"])

print(f"✓ Usuário válido: {usuario=}")
