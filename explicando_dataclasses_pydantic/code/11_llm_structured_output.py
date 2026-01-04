# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "openai>=2.15.0",
#     "pydantic>=2.0.0",
#     "python-dotenv>=1.2.1",
# ]
# ///
"""
LLM Structured Outputs com Pydantic

Exemplo mostrando como usar Pydantic para validar outputs de LLMs
Baseado em: https://platform.openai.com/docs/guides/structured-outputs
"""

from dotenv import load_dotenv

load_dotenv()

# region code
from openai import OpenAI
from datetime import date
from pydantic import BaseModel, Field

client = OpenAI()


class Evento(BaseModel):
    name: str = Field(min_length=2, description="Nome do evento")
    date: date
    participants: list[str] = Field(min_length=1)


response = client.responses.parse(
    model="gpt-5-nano",
    input=[
        {"role": "system", "content": "Extraia as informações do evento."},
        {"role": "user", "content": "Alice e Bob vão a uma feira de ciências na sexta-feira, 28 de outubro de 2026."},
    ],
    text_format=Evento,
)
# endregion code

print(f"{response.output_parsed=}")
print(f"{type(response.output_parsed)=}")
