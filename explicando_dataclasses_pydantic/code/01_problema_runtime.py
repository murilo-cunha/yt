"""Demonstra o problema: type hints não protegem em runtime."""


# region code
def processar_usuario(dados: dict) -> str:
    nome = dados["nome"]
    idade = dados["idade"]
    if idade < 0:
        raise ValueError("Idade não pode ser negativa")
    return f"{nome} tem {idade} anos"


dados = {"nome": "Maria", "idade": 30}  # ok
# dados = {"nome": "João"}  # KeyError - campo faltando
# dados = {"nome": "Ana", "idade": "trinta"}  # TypeError - tipo errado
# dados = {"nome": "Pedro", "idade": -5}  # ValueError - valor inválido
print(processar_usuario(dados))
# endregion code
