# Explicando Chat Templates & Tokenizers

> Código e apresentação para o vídeo "Explicando: Chat Templates & Tokenizers" no [YouTube](https://www.youtube.com/watch?v=ll9R-kaxM64)

Este projeto contém uma apresentação em [Slidev](https://sli.dev) sobre Chat Templates e Tokenizers, baseada no conteúdo do [Hugging Face Smol Course - Unit 1.2](https://huggingface.co/learn/smol-course/unit1/2). A apresentação cobre conceitos essenciais como modelos base vs modelos de instrução, estrutura de mensagens, aplicação de templates, generation prompts, conversas multi-turno, system messages, e boas práticas para trabalhar com LLMs.

## Como executar

Para visualizar a apresentação, você pode executar um dos seguintes comandos na raiz do projeto:

```bash
# Com Deno
deno x @slidev/cli slides.md

# Com npx
npx @slidev/cli slides.md

# Com Bun
bunx @slidev/cli slides.md
```

A apresentação será aberta automaticamente no navegador. Os scripts de exemplo em Python podem ser executados com [uv](https://docs.astral.sh/uv/), com o comando `uv run code/<nome_do_script>.py`.
