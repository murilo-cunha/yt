# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pydantic>=2.0.0",
# ]
# ///
"""
Validação e coerção de tipos no Pydantic
"""

# region code
from pydantic import BaseModel, Field


class Produto(BaseModel):
    nome: str
    preco: float
    em_estoque: bool


class ProdutoStrict(BaseModel):
    nome: str
    preco: float = Field(strict=True)  # sem coerção
    em_estoque: bool


# endregion code

# # Exemplo 1: Coerção útil de tipos
# produto = Produto(
#     nome="Notebook",
#     preco="2500.50",  # string → float
#     em_estoque="yes",  # string → bool
# )
# print(f"✓ {produto.nome}: R$ {produto.preco} (em estoque: {produto.em_estoque})")
# print(f"  Tipos: preco={type(produto.preco)}, em_estoque={type(produto.em_estoque)}")

# # Exemplo 2: Coerção inteligente de bool
# for valor in [1, 0, "true", "false", "yes", "no", "on", "off"]:
#     p = Produto(nome="Teste", preco=10.0, em_estoque=valor)
#     print(f"  '{valor}' → {p.em_estoque}")

# # Exemplo 3: Rejeita conversões impossíveis
# produto = Produto(nome="Mouse", preco="preço inválido", em_estoque=True)
# print(produto)

# # Exemplo 4: Modo strict (sem coerção)
# produto = ProdutoStrict(nome="Teclado", preco="150.00", em_estoque=True)
# print(produto)
