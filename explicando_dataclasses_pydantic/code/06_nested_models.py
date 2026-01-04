# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pydantic>=2.0.0",
# ]
# ///
"""
Models aninhados para estruturas complexas
"""

# region code
from pydantic import BaseModel, Field


class Endereco(BaseModel):
    rua: str
    numero: int
    cidade: str
    estado: str = Field(min_length=2, max_length=2)
    cep: str = Field(pattern=r"^\d{5}-\d{3}$")


class Contato(BaseModel):
    email: str
    telefone: str


class Usuario(BaseModel):
    nome: str
    idade: int = Field(gt=0)
    endereco: Endereco
    contatos: list[Contato]

    def info(self) -> Usuario:
        """Imprime informações do usuário."""
        print(f"✓ Usuário: {self.nome}")
        print(f"  Endereço: {self.endereco.rua}, {self.endereco.numero}")
        print(f"  Cidade: {self.endereco.cidade}/{self.endereco.estado}")
        print(f"  Contatos: {len(self.contatos)}")
        for i, contato in enumerate(self.contatos, 1):
            print(f"    {i}. {contato.email} - {contato.telefone}")
        return self


# endregion code

# Exemplos de uso
usuario_data = {
    "nome": "Maria Silva",
    "idade": 30,
    "endereco": {
        "rua": "Av. Paulista",
        "numero": 1000,
        "cidade": "São Paulo",
        "estado": "SP",
        "cep": "01310-100",
    },
    "contatos": [
        {"email": "maria@example.com", "telefone": "11-99999-9999"},
        {"email": "maria.trabalho@company.com", "telefone": "11-3333-3333"},
    ],
}

# usuario_data = {
#     "nome": "João",
#     "idade": 25,
#     "endereco": {
#         "rua": "Rua ABC",
#         "numero": 100,
#         "cidade": "Rio de Janeiro",
#         "estado": "RIO",
#         "cep": "20000-000",
#     },
#     "contatos": [],
# }

# usuario_data = {
#     "nome": "Ana",
#     "idade": 28,
#     "endereco": {
#         "rua": "Rua XYZ",
#         "numero": 200,
#         "cidade": "Belo Horizonte",
#         "estado": "MG",
#         "cep": "30000000",  # ✗ formato errado
#     },
#     "contatos": [{"email": "ana@example.com", "telefone": "31-99999-9999"}],
# }

usuario = Usuario(**usuario_data).info()
