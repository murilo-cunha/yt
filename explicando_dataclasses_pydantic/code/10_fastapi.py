# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "fastapi>=0.100.0",
#     "uvicorn>=0.23.0",
#     "pydantic>=2.0.0",
# ]
# ///
"""
Pydantic + FastAPI: validação automática

Para rodar:
    uvicorn 10_fastapi:app --reload

Acesse: http://localhost:8000/docs
"""

# region code
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Usuario(BaseModel):
    nome: str = Field(min_length=2, description="Nome do usuário")
    idade: int = Field(ge=18, lt=150, description="Idade positiva")


class UsuarioResponse(BaseModel):
    id: int
    nome: str
    idade: int
    mensagem: str


@app.post("/usuarios", response_model=UsuarioResponse)
def criar_usuario(usuario: Usuario) -> UsuarioResponse:
    """
    FastAPI usa Pydantic para validar entrada E saída

    - Tente com dados válidos: {"nome": "Maria", "idade": 25}
    - Tente com idade negativa: {"nome": "João", "idade": 10}
    - Tente com nome curto: {"nome": "A", "idade": 30}

    Request validado → Response serializado automaticamente
    """
    # Conectar com a base de dados e criar usuário, etc...
    return UsuarioResponse(
        id=1,
        nome=usuario.nome,
        idade=usuario.idade,
        mensagem=f"Usuário {usuario.nome} criado com sucesso!",
    )


# endregion code

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
