---
theme: apple-basic
#background:
title: Dataclasses & Pydantic
mdc: true
addons:
  - fancy-arrow
---

<div class="absolute bottom-10">
  <h1>Explicando</h1>
  <p>Dataclasses & Pydantic</p>
</div>

---

# Prior: Type Hints

Type hints são anotações de tipo no Python

- Introduzidos no Python 3.5 (PEP 484)
- Indicam o tipo esperado de variáveis, parâmetros e retornos
- **Não são obrigatórios** - Python continua sendo dinamicamente tipado
- Ferramentas como IDEs e `mypy` usam para análise estática
- **Não fazem validação em runtime** - são apenas "dicas"

```python {*|1|4-}
def somar(a: int, b: int) -> int:
    return a + b

nome: str = "João"
idade: int = 25
```

<carbon-arrow-right/> Type hints são a base para Pydantic e dataclasses

---
layout: two-cols
---

# Porque Pydantic?

Python types não te protegem em runtime

<br/>

Dados vêm bagunçados:

- **APIs**: campos inconsistentes, tipos errados
- **Usuários**: formulários, inputs
- **Arquivos de configuração / variáveis de ambiente**
- **LLMs**: texto livre

<carbon-arrow-right/> Type hints ajudam ferramentas (IDE, `mypy`), mas **não validam** em runtime.
::right::
O que dá errado:

- `KeyError`, `TypeError`, bugs silenciosos, casos de borda pouco claros
- Você também quer garantias sobre os dados (ex: idade é um inteiro, mas também é positivo)

<<< @/code/01_problema_runtime.py#code {*|1|2-3|4-6}

---
layout: two-cols
---

# O que é Pydantic?

Pydantic = models + validação usando type annotations

- Define um schema usando type annotations do Python
- Pydantic valida e faz parsing da entrada em runtime
- Oferece:
  - Código mais seguro
  - Mensagens de erro claras
  - Serialização limpa (dict/JSON)
  - Suporte de IDE via LSPs

::right::

<br/>

**Fluxo:**

Dados de entrada → `BaseModel` → objeto validado

<<< @/code/02_pydantic_basico.py#code {*|4-6}{maxHeight:'470px',lines:0}

---
layout: two-cols
---

# Dataclasses vs Pydantic

Mesma forma, propósito diferente

**Dataclasses**

- Leve, biblioteca padrão
- Ótimo para objetos internos onde os dados já são confiáveis
- Sem validação em runtime por padrão

**Pydantic**

- Validação em runtime + parsing
- Projetado para dados externos/não confiáveis
- Ecossistema rico de features (settings, JSON, etc.)
- `Field` e todas as propriedades úteis que vêm com ele (incluindo `description`)

::right::

<div class="flex items-center h-full">

<<< @/code/03_dataclass_vs_pydantic.py#code {*|1,6-10|3,12-16|*}{maxHeight:'470px',lines:0}

</div>

---

# Quando usar qual?

**Use dataclasses quando:**

- Modelos de domínio internos
- Você controla os dados
- Dependências mínimas

**Use Pydantic quando:**

- Fronteiras: APIs, requisições web, config/env, ETL, outputs de LLM
- Você precisa de tipos garantidos + restrições

---

# Exemplos: Validação & Coerção de Tipos

Validação + coerção útil

- Converte inputs comuns (`1` → `True`) quando seguro
- Rejeita inputs inválidos com erros claros
- Modo strict opcional (seja explícito quando precisar)

<<< @/code/04_validacao_coercao.py#code {*|4-7|10-13|*}{maxHeight:'280px',lines:0}

---
layout: two-cols
---

# Field Metadata & Constraints

Constraints comunicam intenção

- Adiciona descrições, padrões, exemplos
- Constraints:
  - numéricos: `gt`, `ge`, `lt`, `le`
  - strings: `min_length`, `max_length`, `pattern`
  - listas: `min_length`, `max_length`
  - ...

::right::

<div class="flex items-center h-full">

<<< @/code/05_field_constraints.py#code {*|5-7|8-12|13-16|17-19|*}{maxHeight:'470px',lines:0}

</div>

---
layout: two-cols
---

# Nested Models

<br/>

Dados complexos? <carbon-arrow-right/> Componha models

- Models podem incluir outros models
- Ótimo para payloads de API, documentos, estruturas hierárquicas
- Modelo mental mais simples

::right::

<<< @/code/06_nested_models.py#code {*|4-9|12-14|17-21|23-31|*}{maxHeight:'470px',lines:0}

---
layout: two-cols
---

# Custom Validators

<br/>

Regras customizadas, por exemplo:

- Valida relacionamentos (ex: `start_date <= end_date`)
- Normaliza inputs (remove espaços, força formatos)
- Podem ser executadas **antes**, **depois**, incluir ou não as validações do Pydantic
- Podem ser executadas no level dos `Field` or `Model` (caso dependa de vários fields)

<carbon-arrow-right/> Mais informações: https://docs.pydantic.dev/latest/concepts/validators/

::right::

<<< @/code/07_custom_validators.py#code {22-26|23,14-19|26,28-37|24-25,39-44}{maxHeight:'470px',lines:0}

---
layout: two-cols
---

# Serialização

<br/>

De/para dict + JSON

- Parse de dict/JSON
- Export para dict/JSON
- Útil para APIs, armazenamento, logging

::right::

<br/>

<<< @/code/08_serializacao.py#code {*}{maxHeight:'470px',lines:0}

---
layout: two-cols
---

# Settings Management

<br/>

Configuração de variáveis de ambiente

- Centraliza configuração
- Parsing tipado de env vars
- Evita `os.environ[...]` frágil espalhado pelo código

::right::

<<< @/code/09_settings.py#code {*|13,15|19-23}{maxHeight:'470px',lines:0}

---
layout: two-cols
---

# Pydantic + FastAPI

FastAPI usa Pydantic como sua espinha dorsal de dados

- **Validação automática de requisições**
  - Request bodies e query params validados antes do seu endpoint executar
- **Documentação OpenAPI/Swagger automática**
  - Models se tornam schemas da API
  - Descrições de campos se tornam documentação
- **Respostas type-safe**
  - Response models garantem output consistent
- **Erros se tornam HTTP 422**
  - Clientes recebem feedback estruturado

::right::

<<< @/code/10_fastapi.py#code {*|4|7-9,12-16|19-20|20,31-36}{maxHeight:'470px',lines:0}

---

# LLMs produzem texto; apps precisam de dados estruturados

<br/>

<div class="flex items-stretch gap-16">
  <div class="flex-1 flex items-center justify-center w-1/3" data-id="openai">
      <img src="https://www.svgrepo.com/show/306500/openai.svg" alt="OpenAI Logo" class="h-28 invert" />
  </div>

  <div class="flex-1 w-1/3" data-id="json">

```json
{
  "name": "Feira de ciências",
  "date": "2026-08-28",
  "participants": ["Alice","Bob"]
}
```

  </div>

  <div class="flex-1 w-1/3" data-id="pydantic">

```python
Evento(
    name="Feira de ciências",
    date=datetime.date(2026, 8, 28),
    participants=["Alice", "Bob"],
)
```

  </div>
</div>

<FancyArrow q1="[data-id=openai]" q2="[data-id=json]" v-click />
<FancyArrow q1="[data-id=json]" q2="[data-id=pydantic]" v-click />
<FancyArrow q1="[data-id=pydantic]" q2="[data-id=openai]" arc="-0.25" pos1="top" pos2="topright" v-click />

<br/>

<<< @/code/11_llm_structured_output.py#code {*|8-11|14-21|20}{maxHeight:'220px',lines:1}

---
layout: center
class: text-center
---

# Conclusões

<br/>

Type hints ≠ validação em runtime

Pydantic transforma annotations em **garantias em runtime**

Melhor em fronteiras: APIs, config, ETL, e outputs de LLM

Integração com FastAPI é um grande ganho de produtividade

---
# Próximos passos

Onde aprender a seguir

- [Documentação oficial](https://docs.pydantic.dev/latest/)
- [Explore a documentação do FastAPI](https://fastapi.tiangolo.com/pt/)
- Experimente com LLMs: OpenAI, Anthropic, Gemini, Instructor, Pydantic AI, etc.

---
layout: center
class: text-center
---

# Obrigado! 🎉
