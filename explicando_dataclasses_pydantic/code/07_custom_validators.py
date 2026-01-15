# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pydantic>=2.0.0",
# ]
# ///
"""
Validators customizados para lógica de negócio
"""

# region code
from datetime import date
from typing import Annotated

from pydantic import (
    AfterValidator,
    BaseModel,
    Field,
    ValidationError,
    field_validator,
    model_validator,
)


def validar_titulo(v: str) -> str:
    """Remove espaços extras e valida tamanho mínimo"""
    v = v.strip()
    if len(v) < 3:
        raise ValueError("Título deve ter pelo menos 3 caracteres")
    return v


class Evento(BaseModel):
    titulo: Annotated[str, AfterValidator(validar_titulo)]
    data_inicio: date
    data_fim: date
    email_participantes: list[str] = Field(min_length=1)

    @field_validator("email_participantes")
    @classmethod
    def validar_participantes(cls, emails: list[str]) -> list[str]:
        """Remove duplicatas e normaliza emails"""
        emails_unicos = {e.strip().lower() for e in emails}
        dominios_permitidos = ["example.com", "company.com"]
        dominio_emails = [email.split("@")[-1] for email in emails_unicos]
        if any(d not in dominios_permitidos for d in dominio_emails):
            print(set(dominio_emails))
            raise ValueError(f"Domínio deve ser um de: {dominios_permitidos}")
        return [email for email in emails_unicos]

    @model_validator(mode="after")
    def validar_datas(self):
        """Valida que data_fim >= data_inicio"""
        if self.data_fim < self.data_inicio:
            raise ValueError("Data de fim deve ser >= data de início")
        return self


# endregion code

evento = Evento(
    titulo="  Workshop Python  ",  # será normalizado (remove espaços)
    data_inicio=date(2025, 1, 10),
    data_fim=date(2025, 1, 12),
    email_participantes=[  # duplicatas removidas, normalizados
        "maria@example.com",
        "joao@company.com",
        "  MARIA@example.com  ",
    ],
)
# evento = Evento(
#     titulo="Conferência DevOps",
#     data_inicio=date(2025, 2, 1),
#     data_fim=date(2025, 2, 1),  # mesmo dia é válido
#     email_participantes=["admin@company.com"],
# )
# evento = Evento(
#     titulo="  AB  ",  # após strip() tem apenas 2 caracteres
#     data_inicio=date(2025, 1, 10),
#     data_fim=date(2025, 1, 12),
#     email_participantes=["maria@example.com"],
# )
# evento = Evento(
#     titulo="Evento Teste",
#     data_inicio=date(2025, 1, 12),
#     data_fim=date(2025, 1, 10),  # fim antes do início
#     email_participantes=["joao@company.com"],
# )
# evento = Evento(
#     titulo="Meetup Python",
#     data_inicio=date(2025, 3, 1),
#     data_fim=date(2025, 3, 1),
#     email_participantes=["usuario@gmail.com"],  # domínio não permitido
# )
# evento = Evento(
#     titulo="Workshop Vazio",
#     data_inicio=date(2025, 4, 1),
#     data_fim=date(2025, 4, 2),
#     email_participantes=[],  # min_length=1
# )
print(f"✓ Evento: {evento.titulo}")
print(f"  Datas: {evento.data_inicio} até {evento.data_fim}")
print(f"  Emails: {evento.email_participantes}")
