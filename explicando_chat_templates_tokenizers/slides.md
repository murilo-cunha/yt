---
theme: apple-basic
background: https://raw.githubusercontent.com/huggingface/smol-course/refs/heads/main/banner.png
transition: slide-left
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
layout: default
---

# O que vamos ver hoje?

<Toc maxDepth="1"></Toc>

<!--
Preparei uma apresentação bem prática e objetiva. Vamos cobrir desde os conceitos básicos até exemplos avançados.
Todo o código estará disponível para vocês testarem depois.
-->

---
transition: slide-up
---

# Modelos Base vs Modelos de Instrução

Entendendo a diferença fundamental

- **Modelo Base** (`SmolLM3-3B-Base`)
  - Treinado em texto bruto
  - Prevê o próximo token
  - Completa sequências de texto

- **Modelo de Instrução** (`SmolLM3-3B`)
  - Fine-tuned para seguir instruções
  - Entende perguntas e comandos
  - Responde como assistente

<!--
A diferença é crucial: modelos base apenas continuam texto, enquanto modelos de instrução entendem contexto de conversa.
Os chat templates são a ponte entre esses dois mundos - eles ensinam o modelo a estruturar conversas.
-->

---
layout: two-cols
---

# A Transformação

Do texto bruto para conversas estruturadas

::left::

**Modelo Base**
```
Input: "O tempo hoje está"
Output: "ensolarado e quente"
```

Apenas continua o texto

::right::

**Modelo de Instrução**
```
Input: "Como está o tempo?"
Output: "Posso verificar para você..."
```

Entende e responde

<!--
Vejam a diferença: o modelo base apenas completa frases. O modelo de instrução entende que é uma pergunta e responde adequadamente.
Essa transformação acontece através de supervised fine-tuning usando chat templates.
-->

---

# O que são Chat Templates?

Formato estruturado para conversas

- **Definição**: "Gramática" para estruturar interações
- **Função**: Ensina modelos a distinguir papéis
- **Padrão**: SmolLM3 usa ChatML (Chat Markup Language)
- **Benefício**: Consistência e clareza

```xml
<|im_start|>system
Você é um assistente prestativo.<|im_end|>
<|im_start|>user
Olá!<|im_end|>
<|im_start|>assistant
Como posso ajudar?<|im_end|>
```

<!--
Chat templates são como regras gramaticais para conversas com IA. 
Eles definem como estruturar mensagens, separar diferentes papéis (sistema, usuário, assistente).
O formato ChatML usa tokens especiais que marcam início e fim de cada mensagem.
-->

---
layout: two-cols
---

# Usando Pipeline - A forma mais fácil

Abstração que gerencia tudo automaticamente

<<< @/code/01_pipeline_basico.py

::right::

<div class="mt-12">

**O Pipeline faz:**
- Aplica chat template
- Tokeniza mensagens
- Gerencia geração
- Retorna output estruturado

</div>

<!--
O pipeline é a forma mais simples de usar LLMs. Ele esconde toda a complexidade dos chat templates.
Você só precisa passar uma lista de mensagens e ele cuida do resto.
Perfeito para começar ou para uso em produção.
-->

---

# Estrutura de Mensagens

Anatomia de uma conversa

<<< @/code/02_estrutura_mensagens.py

**Tipos de Mensagem:**
- `system`: Define comportamento do modelo
- `user`: Perguntas e comandos do usuário
- `assistant`: Respostas da IA
- `tool`: Resultados de funções (avançado)

<!--
Cada mensagem tem dois campos essenciais: role e content.
O role identifica quem está falando - sistema, usuário ou assistente.
Essa estrutura simples mas poderosa permite conversas complexas e multiturno.
-->

---

# Aplicando Chat Templates Manualmente

Controle direto sobre a formatação

<<< @/code/03_aplicar_template.py

**Parâmetros importantes:**
- `tokenize=False`: Retorna string em vez de tokens
- `add_generation_prompt=True`: Adiciona prompt para resposta

<!--
Quando você precisa de mais controle, pode aplicar o chat template manualmente.
O tokenizer já vem configurado com o template correto para cada modelo.
Esse é o método usado internamente pelo pipeline.
-->

---
layout: two-cols
---

# Generation Prompt

Controlando quando o modelo responde

<<< @/code/04_generation_prompt.py {all|14-18|21-25}

::right::

<div class="mt-12">

**Quando usar:**

✅ `True` → Inferência  
❌ `False` → Treinamento

</div>

<!--
O generation prompt é crucial! Ele diz ao modelo "agora é sua vez de falar".
Sem ele, o modelo pode continuar a mensagem do usuário em vez de responder.
Para treinamento usamos False porque já temos as respostas completas.
-->

---

# Modo Thinking do SmolLM3

Raciocínio visível vs invisível

<<< @/code/05_thinking_mode.py

**Benefícios do Thinking Mode:**
- Mostra processo de raciocínio
- Útil para tarefas complexas
- Transparência nas respostas
- Debugging mais fácil

<!--
Uma feature especial do SmolLM3 é o modo thinking.
Ele pode mostrar ou esconder o raciocínio interno.
Perfeito para matemática, lógica, ou quando você quer entender como o modelo chegou à resposta.
-->

---

# Conversas Multi-turno

Mantendo contexto através de múltiplas interações

<<< @/code/06_conversa_multiturno.py

<!--
Conversas multi-turno são fundamentais para assistentes úteis.
O modelo mantém contexto de mensagens anteriores.
Você simplesmente adiciona novas mensagens à lista e passa de volta para o pipeline.
-->

---

# System Messages

Definindo o comportamento do modelo

<<< @/code/07_system_messages.py

**Dicas para System Messages:**
- Seja específico e claro
- Defina limites e expectativas
- Use exemplos quando possível
- É a primeira mensagem da conversa

<!--
System messages são super poderosos - eles definem toda a personalidade do modelo.
Podem transformar o mesmo modelo em um assistente técnico, criativo, ou profissional.
Invista tempo criando bons system prompts - faz toda a diferença!
-->

---

# Formato ChatML - Estrutura

Tokens especiais que delimitam conversas

```xml
<|im_start|>system
Você é um assistente técnico focado em programação.<|im_end|>
<|im_start|>user
Olá!<|im_end|>
<|im_start|>assistant
Como posso ajudar?<|im_end|>
<|im_start|>user
Explique funções em Python.<|im_end|>
<|im_start|>assistant
```

**Componentes:**
- `<|im_start|>` e `<|im_end|>`: Delimitadores
- Roles: system, user, assistant, tool
- Content: Conteúdo entre os delimitadores

<!--
O ChatML usa tokens especiais bem definidos.
Esses tokens ensinam o modelo onde cada mensagem começa e termina.
É importante não adicionar esses tokens manualmente - deixe o template fazer isso!
-->

---
layout: two-cols
---

# Continue Final Message

Controlando continuação de respostas

::left::

**Caso de uso: JSON**
```python
messages = [
    {"role": "user", 
     "content": "Responda em JSON"},
    {"role": "assistant", 
     "content": '{"nome": "'}
]

# continue_final_message=True
# Modelo completa: João",
```

::right::

**Aplicações:**
- Output estruturado
- Completar código
- Guiar raciocínio
- Forçar formatos

<!--
Continue final message é uma técnica avançada mas muito útil.
Você "preenche parcialmente" a resposta do assistente e o modelo completa.
Ótimo para garantir formato JSON, completar código, ou guiar o raciocínio passo a passo.
-->

---

# Parâmetros de Geração

Controlando a criatividade do modelo

```python
generation_config = {
    "max_new_tokens": 200,      # Máximo de tokens a gerar
    "temperature": 0.8,          # Criatividade (0-2)
    "do_sample": True,           # Usar sampling
    "top_p": 0.9,               # Nucleus sampling
    "repetition_penalty": 1.1    # Evitar repetição
}
```

**Temperature:**
- 0.1-0.3: Respostas focadas e determinísticas
- 0.7-0.9: Balanceado (recomendado)
- 1.5-2.0: Muito criativo/aleatório

<!--
Os parâmetros de geração são como você afina o comportamento do modelo.
Temperature é o mais importante - baixa para tarefas factuais, alta para criatividade.
Top_p e repetition_penalty ajudam a manter respostas naturais e variadas.
-->

---

# Function Calling / Tool Usage

Permitindo o modelo usar ferramentas externas

```python
tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Obtém clima atual de uma localização",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string"},
                "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
            },
            "required": ["location"]
        }
    }
}]
```

<!--
Function calling permite que LLMs interajam com o mundo externo.
O modelo aprende quando e como chamar funções baseado nas descrições.
Você define as ferramentas disponíveis e o modelo decide quando usá-las.
-->

---

# Boas Práticas - Template Consistency

Regras de ouro para usar chat templates

✅ **FAÇA:**
- Use o mesmo template para treino e inferência
- Use `add_generation_prompt=True` para inferência
- Use `add_generation_prompt=False` para treino
- Deixe o tokenizer gerenciar tokens especiais
- Teste templates antes de treinar

❌ **NÃO FAÇA:**
- Adicionar tokens especiais manualmente
- Misturar diferentes formatos de template
- Ignorar system messages importantes
- Esquecer de validar estrutura de mensagens

<!--
Consistência é crucial! Usar templates diferentes entre treino e inferência quebra o modelo.
Nunca adicione tokens especiais manualmente - o template já faz isso.
Essas práticas podem parecer simples, mas evitam 90% dos problemas comuns.
-->

---

# Debugging de Templates

Inspecionando o que está acontecendo

```python
# Ver o template do modelo
print(tokenizer.chat_template)

# Ver tokens especiais
print(f"BOS: {tokenizer.bos_token}")
print(f"EOS: {tokenizer.eos_token}")

# Aplicar template e ver resultado
formatted = tokenizer.apply_chat_template(
    messages, 
    tokenize=False
)
print(repr(formatted))  # Mostra caracteres de escape
```

<!--
Quando algo não funciona, é hora de debugar.
Inspecionar o template ajuda a entender o que está acontecendo.
O repr() mostra todos os caracteres especiais, muito útil para debugging.
-->

---

# Casos de Uso Reais

Aplicações práticas de chat templates

1. **Chatbots de Atendimento**
   - System message define tom profissional
   - Multi-turno para contexto

2. **Assistentes de Código**
   - System message com expertise técnica
   - Continue final message para completar código

3. **Tutores Educacionais**
   - Thinking mode para mostrar raciocínio
   - System message pedagógico

4. **Agentes com Ferramentas**
   - Function calling para APIs
   - Tool messages para feedback

<!--
Templates não são só teoria - têm aplicações práticas importantes.
Cada caso de uso se beneficia de diferentes aspectos dos templates.
A chave é escolher a combinação certa de features para seu problema.
-->

---

# Armadilhas Comuns

Erros frequentes e como evitá-los

❌ **Template Mismatch**
- Usar template diferente do que o modelo foi treinado

❌ **Tokens Duplicados**
- Adicionar tokens quando template já inclui

❌ **System Message Ausente**
- Não fornecer contexto suficiente

❌ **Generation Prompt Errado**
- Usar `True` quando deveria ser `False` (ou vice-versa)

❌ **Context Overflow**
- Não gerenciar tamanho de conversas longas

<!--
Aprenda com os erros dos outros! Essas são as armadilhas mais comuns.
Template mismatch é provavelmente o erro número 1 - sempre confira!
Context overflow acontece em conversas muito longas - implemente truncamento.
-->

---
layout: two-cols
---

# Performance e Otimização

Dicas para produção

::left::

**Otimizações:**
- Cache templates formatados
- Batch processing
- Truncamento inteligente
- Monitore token usage

::right::

**Métricas importantes:**
- Taxa de erro em templates
- Latência média
- Token usage
- Qualidade de respostas

<!--
Em produção, performance importa muito.
Cachear templates formatados economiza processamento.
Monitorar métricas ajuda a identificar problemas cedo.
-->

---

# Próximos Passos

Onde ir a partir daqui

📚 **Aprender:**
- Supervised Fine-Tuning (próximo tópico)
- Preference Alignment (RLHF/DPO)
- Custom template creation
- Multimodal templates

🔧 **Praticar:**
- Criar seu próprio chatbot
- Fine-tune SmolLM3 para seu domínio
- Experimentar com thinking mode
- Implementar function calling

<!--
Chat templates são a base - agora você está pronto para o próximo nível.
Supervised fine-tuning usa tudo que vimos hoje para treinar modelos.
A melhor forma de aprender é praticando - escolha um projeto e mãos à obra!
-->

---

# Recursos e Documentação

Links úteis para aprofundar

**Documentação Oficial:**
- [Chat Templates Basics](https://huggingface.co/docs/transformers/chat_template_basics)
- [SmolLM3 Model Card](https://huggingface.co/HuggingFaceTB/SmolLM3-3B)
- [TRL Documentation](https://huggingface.co/docs/trl)

**Comunidade:**
- [Hugging Face Forum](https://discuss.huggingface.co/)
- [Discord](https://discord.gg/UrrTSsSyjb)

**Dataset:**
- [SmolTalk2](https://huggingface.co/datasets/HuggingFaceTB/smoltalk2)

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

Perguntas?

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
