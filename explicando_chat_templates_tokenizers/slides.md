---
theme: apple-basic
background: https://raw.githubusercontent.com/huggingface/smol-course/refs/heads/main/banner.png
title: Chat Templates & Tokenizers
mdc: true
layout: intro-image
image: 'https://raw.githubusercontent.com/huggingface/smol-course/refs/heads/main/banner.png'
---

<div class="absolute bottom-10">
  <h1>Explicando</h1>
  <p>Chat Templates & Tokenizers</p>
</div>


<!--
Bem-vindos! Hoje vamos explorar chat templates e tokenizers, conceitos fundamentais para trabalhar com LLMs.
Vamos ver como funcionam os modelos de instrução e como estruturar conversas de forma eficaz.
-->

---
layout: two-cols
---

# Modelos Base vs Modelos de Instrução

Entendendo a diferença fundamental

<v-clicks>

- **Modelo Base** (`SmolLM3-3B-Base`)
  - Treinado em texto bruto
  - Prevê o próximo token
  - Completa sequências de texto

<div class="mt-8"></div>

- **Modelo de Instrução** (`SmolLM3-3B`)
  - Fine-tuned para seguir instruções
  - Entende perguntas e comandos
  - Responde como assistente

</v-clicks>

::right::


<div class="flex flex-col gap-4">
<v-click>
  <div>
    <p class="text-sm mb-2 font-semibold">Next Token Prediction:</p>
    <img src="https://jalammar.github.io/images/gpt3/05-gpt3-generate-output-context-window.gif" alt="Next Token Prediction" class="rounded w-full">
  </div>
</v-click>

<v-click>
  
  <div>
    <p class="text-sm mb-2 font-semibold">Conversation Structure:</p>
    
```json
[
  {"role": "user", 
   "content": "Como está o tempo?"},
  {"role": "assistant", 
   "content": "Posso verificar..."}
]
```
  </div>
</v-click>
</div>

<!--
A diferença é crucial: modelos base apenas continuam texto, enquanto modelos de instrução entendem contexto de conversa.
Os chat templates são a ponte entre esses dois mundos - eles ensinam o modelo a estruturar conversas.
-->

---

# Papéis em Chat Templates

Entendendo system, user e assistant

- **System**: Define comportamento e personalidade do modelo
- **User**: Mensagens do usuário/cliente
- **Assistant**: Respostas geradas pelo modelo

<<< @/code/07_system_messages.py#code {*}{maxHeight:'250px'}

<!--
Cada papel tem sua função específica:
- System message é como dar instruções permanentes ao modelo
- User é sempre quem está fazendo perguntas
- Assistant é o modelo respondendo
É importante manter essa estrutura para o modelo entender o contexto corretamente.
# Mensagens de sistema definem o comportamento do modelo
# São a primeira mensagem e influenciam toda a conversa
-->

---

# Usando Pipeline - A forma mais fácil

Abstração que gerencia tudo automaticamente

<<< @/code/01_pipeline_basico.py#code

<!--**O Pipeline faz:**
- Aplica chat template
- Tokeniza mensagens
- Gerencia geração
- Retorna output estruturado

O pipeline é a forma mais simples de usar LLMs. Ele esconde toda a complexidade dos chat templates.
Você só precisa passar uma lista de mensagens e ele cuida do resto.
Perfeito para começar ou para uso em produção.
-->

---

# Aplicando Templates Sem Chamar o LLM

Útil para preparação de dados e treinamento

O pipeline automaticamente transforma mensagens JSON em texto formatado usando chat templates por trás dos planos.

<<< @/code/03_aplicar_template.py#code {*}{maxHeight:'320px'}

<!--
Quando preparamos dados para treinamento, não queremos o generation prompt.
Isso permite que o modelo aprenda a gerar a resposta do assistente a partir do template completo.
É especialmente útil para criar datasets de fine-tuning.
False = preparar dados | True = gerar respostas
-->

---

# Convertendo Conversas

## Formato JSON
```json {*|2|3|6|8|*}
[
    {"role": "system", "content": "Você é um assistente técnico."},
    {"role": "user", "content": "Explique o que é um chat template?"},
    {
        "role": "assistant",
        "content": "Eles padronizam a conversão de diálogos em um formato de texto que LLMs consiguem entender e processar corretamente.",
    },
    {"role": "user", "content": "Como é esse formato?"},
]
```

## Formato ChatML

```xml {*|10|13|15|17|18}{at:1, lines:true, maxHeight:'190px'}
<|im_start|>system
## Metadata

Knowledge Cutoff Date: June 2025
Today Date: 02 January 2026
Reasoning Mode: /think

## Custom Instructions

Você é um assistente técnico.

<|im_start|>user
Explique o que é um chat template?<|im_end|>
<|im_start|>assistant
Eles padronizam a conversão de diálogos em um formato de texto que LLMs consiguem entender e processar corretamente.<|im_end|>
<|im_start|>user
Como é esse formato?<|im_end|>
<|im_start|>assistant
```

---

# Generation Prompt

Controlando início de resposta do modelo

O parâmetro `add_generation_prompt` adiciona tokens que indicam que é a vez do assistente responder.

<<< @/code/04_generation_prompt.py#code {*|13,18}{maxHeight:'340px'}

<!--
O generation prompt é crucial para indicar ao modelo que deve começar a responder.
Sem ele, o modelo pode não entender que é sua vez de falar.
Use True para inferência (gerar respostas) e False para preparar dados de treino.
-->

---

# Continue Final Message

Controle avançado de resposta

O parâmetro `continue_final_message=True` faz o modelo **continuar** a última mensagem ao invés de iniciar uma nova.

<<< @/code/08_continue_final_message.py#code {*|8|13,18}{maxHeight:'315px'}

<!--
Continue final message é uma técnica avançada de "prefilling" - você começa a resposta do assistente.
Muito útil para forçar formato específico de saída, como JSON ou código.
O modelo vai continuar exatamente de onde você parou, mantendo o formato.
Não pode usar add_generation_prompt=True junto com continue_final_message=True.
-->

---

# Aplicações Práticas - Continue Final Message

Casos de uso reais

<v-clicks>

<div>

**1. Saída Estruturada (JSON)**
```python
{"role": "assistant", "content": '{"answer": "'}
```

<carbon-arrow-right/> Modelo completa: `Paris", "confidence": 0.95}`

</div>
<div>

**2. Completar Código**
```python
{"role": "assistant", "content": "def factorial(n):\n    return n * "}
```

Modelo completa: `factorial(n-1) if n > 1 else 1`

</div>
<div>

**3. Raciocínio Guiado**
```python
{"role": "assistant", "content": "Vou resolver passo a passo:\n\nPasso 1: "}
```

<carbon-arrow-right/>  Modelo segue a estrutura sugerida

</div>
</v-clicks>

<!--
Continue final message é poderoso para guiar o formato de saída.
Use para JSON, código, ou qualquer formato estruturado.
Também útil para guiar o modelo através de raciocínio passo a passo.
Lembre: a última mensagem deve ter role "assistant".
-->

---

# Recap: Parâmetros de `apply_chat_template`


```python
json_messages = [
    {"role": "user", "content": "Formate a resposta em JSON"},
    {"role": "assistant", "content": '{"name": "'},
]
```

<div class="grid grid-cols-3 gap-4">
<v-click>
  <div>
    <h3 class="text-lg font-semibold mb-2">add_generation_prompt=false</h3>
    
```python {4,11}
>>> tokenizer.apply_chat_template(
    json_messages,
    tokenize=False,
    add_generation_prompt=False,
)
"""
...
<|im_start|>user
Formate a resposta em JSON<|im_end|>
<|im_start|>assistant
{"name": "<|im_end|>
"""
```
  </div>
</v-click>
<v-click>
  <div>
    <h3 class="text-lg font-semibold mb-2">add_generation_prompt=true</h3>
    
```python {4,11-12}
>>> tokenizer.apply_chat_template(
    json_messages,
    tokenize=False,
    add_generation_prompt=True,
)
"""
...
<|im_start|>user
Formate a resposta em JSON<|im_end|>
<|im_start|>assistant
{"name": "<|im_end|>
<|im_start|>assistant
"""
```
  </div>
</v-click>
<v-click>
  <div>
    <h3 class="text-lg font-semibold mb-2">continue_final_message=true</h3>

```python {4,11}
>>> tokenizer.apply_chat_template(
    json_messages,
    tokenize=False,
    continue_final_message=True,
)
"""
...
<|im_start|>user
Formate a resposta em JSON<|im_end|>
<|im_start|>assistant
{"name": "
"""
```

  </div>
</v-click>
</div>

---

# Thinking Mode

Expondo raciocínio do modelo

Alguns modelos suportam mostrar seu processo de pensamento antes da resposta final.

<<< @/code/05_thinking_mode.py#code {*|12}

<!--
Thinking mode é uma feature avançada que permite ver como o modelo está raciocinando.
Útil para debugging, educação e para construir confiança nas respostas.
Nem todos os modelos suportam - verifique a documentação do modelo.
O modelo gera primeiro seu raciocínio interno, depois a resposta para o usuário.
-->

---

# Function Calling / Tool Usage

Integrando LLMs com ferramentas externas

Chat templates suportam **function calling** - permitindo que modelos chamem APIs e ferramentas.

<<< @/code/10_tool_definition.py#code {*}{maxHeight:'340px'}

<!--
Function calling permite que LLMs interajam com o mundo real.
Ferramentas são definidas usando JSON Schema - especificando nome, descrição e parâmetros.
O modelo aprende quando e como chamar cada ferramenta baseado na descrição.
Parâmetros obrigatórios garantem que o modelo forneça todas as informações necessárias.
-->

---

# Como Function Calling Afeta o Template

O template injeta definições de ferramentas no system message

<<< @/code/09_function_calling.py#code {*|6|7|9-10|11-20|22-26|27-30}{maxHeight:'400px'}

<!--
Quando você passa tools para apply_chat_template, acontece mágica!
O template automaticamente injeta as definições no system message em formato XML.
O modelo aprende a gerar tool_calls quando precisa de informações externas.
Você executa a ferramenta e retorna o resultado com role "tool".
O modelo então gera a resposta final usando o resultado da ferramenta.
-->

---

# Customização Avançada de Templates

Para casos de uso especializados

Você pode criar **templates customizados** usando sintaxe Jinja2:

```python {*}{maxHeight:'370px'}
custom_template = """
{%- for message in messages %}
    {%- if message['role'] == 'system' %}
        {%- set system_message = message['content'] %}
    {%- endif %}
{%- endfor %}
{%- if system_message is defined %}
<|system|>{{ system_message }}<|end|>
{%- endif %}
{%- for message in messages %}
    {%- if message['role'] == 'user' %}
<|user|>{{ message['content'] }}<|end|>
    {%- elif message['role'] == 'assistant' %}
<|assistant|>{{ message['content'] }}<|end|>
    {%- endif %}
{%- endfor %}
{%- if add_generation_prompt %}
<|assistant|>
{%- endif %}
"""
tokenizer.chat_template = custom_template
```

<!--
Templates customizados são para casos muito específicos.
Use Jinja2 para criar lógica condicional e loops.
Cuidado: templates errados podem quebrar completamente o modelo!
Só customize se realmente necessário - os templates padrão funcionam muito bem.
Útil para: formatos proprietários, integrações especiais, ou experimentos de pesquisa.
-->

---

# Recursos e Documentação

Links úteis para aprofundar

Baseado no conteúdo do [Hugging Face Smol Course - Unit 1.2](https://huggingface.co/learn/smol-course/unit1/2)

**Documentação Oficial:**
- [Chat Templates Basics](https://huggingface.co/docs/transformers/main/en/chat_template_basics)
- [SmolLM3 Model Card](https://huggingface.co/HuggingFaceTB/SmolLM3-3B)
- [TRL Documentation](https://huggingface.co/docs/trl)

<!--
Deixo aqui recursos excelentes para vocês continuarem estudando.
A documentação do Hugging Face é muito completa e bem escrita.
A comunidade é super ativa - não tenham medo de fazer perguntas!
-->

---
layout: center
class: text-center
---

# Obrigado! 🎉

<div class="pt-12">
  <span class="text-sm opacity-75">
    Baseado no conteúdo: Hugging Face Smol Course - Unit 1.2
  </span>
</div>

<!--
E é isso! Espero que tenham gostado e aprendido bastante.
Chat templates podem parecer simples, mas são fundamentais para trabalhar bem com LLMs.
Fiquem à vontade para perguntar qualquer coisa!
-->
