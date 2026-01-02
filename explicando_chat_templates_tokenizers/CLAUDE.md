# Histórico do Projeto - Chat Templates & Tokenizers

## Objetivo do Projeto

Criar uma apresentação em Slidev (20 minutos) sobre Chat Templates e Tokenizers, baseada no conteúdo do Hugging Face Smol Course - Unit 1.2.

**Link de referência**: https://huggingface.co/learn/smol-course/unit1/2

## O que foi criado

### 1. Apresentação em Slidev (`slides.md`)

Apresentação completa em **português brasileiro** cobrindo:
- Modelos Base vs Modelos de Instrução
- O que são Chat Templates
- Uso de Pipeline (forma mais fácil)
- Estrutura de Mensagens
- Aplicação de Chat Templates
- Generation Prompts
- Modo Thinking do SmolLM3
- Conversas Multi-turno
- System Messages
- Formato ChatML
- Continue Final Message
- Parâmetros de Geração
- Function Calling / Tool Usage
- Boas Práticas
- Debugging
- Casos de Uso Reais
- Armadilhas Comuns
- Performance e Otimização
- Próximos Passos e Recursos

**Características**:
- Todo conteúdo em português brasileiro
- Notas de voz over em comentários de cada slide
- Código importado de arquivos externos (snippets)
- Estrutura simples e didática

### 2. Scripts Python (`code/`)

7 scripts de exemplo demonstrando diferentes conceitos:

1. `01_pipeline_basico.py` - Uso básico do pipeline
2. `02_estrutura_mensagens.py` - Estrutura de mensagens (demonstrativo)
3. `03_aplicar_template.py` - Aplicação manual de templates
4. `04_generation_prompt.py` - Diferença entre com/sem generation prompt
5. `05_thinking_mode.py` - Modo thinking do SmolLM3 (demonstrativo)
6. `06_conversa_multiturno.py` - Conversas com múltiplos turnos
7. `07_system_messages.py` - Tipos de system messages (demonstrativo)

**Características dos scripts**:
- Metadados inline para uv (PEP 723)
- Python `>=3.14`
- Dependências pinadas: `transformers>=4.46.0`
- Código em inglês (nomes de variáveis)
- Comentários em português
- Créditos ao Hugging Face Smol Course como docstring
- Apenas dependências realmente utilizadas em cada script

## Como usar

### Visualizar a apresentação

```bash
# Instalar dependências do Slidev (se necessário)
npm install

# Iniciar apresentação
npx slidev slides.md
```

### Executar os scripts

Com uv (recomendado):

```bash
uv run code/01_pipeline_basico.py
uv run code/03_aplicar_template.py
# etc...
```

O uv criará automaticamente um ambiente virtual com as dependências necessárias.

## Estrutura de Arquivos

```
.
├── slides.md                    # Apresentação principal
├── code/                        # Scripts de exemplo
│   ├── 01_pipeline_basico.py
│   ├── 02_estrutura_mensagens.py
│   ├── 03_aplicar_template.py
│   ├── 04_generation_prompt.py
│   ├── 05_thinking_mode.py
│   ├── 06_conversa_multiturno.py
│   └── 07_system_messages.py
└── CLAUDE.md                    # Este arquivo
```

## Tecnologias Utilizadas

- **Slidev**: Framework de apresentações para desenvolvedores
- **Python**: Exemplos de código
- **uv**: Gerenciador de pacotes Python (inline scripts)
- **Transformers**: Biblioteca Hugging Face para LLMs

## Créditos

Todo o conteúdo é baseado no **Hugging Face Smol Course - Unit 1.2**:
https://huggingface.co/learn/smol-course/unit1/2

## Notas Adicionais

- A apresentação está preparada para voice over (notas nos comentários)
- Scripts podem ser executados independentemente
- Conteúdo focado em didática e simplicidade
- Exemplos práticos e aplicáveis
