# Explicando uv

> Código e exemplos para o vídeo "Explicando: uv" no [YouTube](https://www.youtube.com/watch?v=ZtIs6LWogxI)

Este projeto contém exemplos práticos sobre [uv](https://docs.astral.sh/uv/), o gerenciador de pacotes e projetos Python (extremamente rápido escrito em Rust). O projeto demonstra como usar uv para gerenciar dependências, ambientes virtuais e executar scripts Python.

## Como executar

Este projeto inclui um devcontainer configurado para facilitar o desenvolvimento. Você pode:

1. Abrir o projeto no VS Code (ou equivalente) com a extensão DevContainers instalada
2. Usar o comando "Reopen in Container" para iniciar o ambiente de desenvolvimento

Alternativamente, se você já tem uv instalado localmente, pode executar os scripts diretamente:

```bash
# Executar um script
uv run main.py
uv run script.py

# Instalar dependências
uv sync

# Adicionar novas dependências
uv add <package-name>
```

## Recursos

- [Documentação oficial do uv](https://docs.astral.sh/uv/)
- [Vídeo no YouTube](https://www.youtube.com/watch?v=ZtIs6LWogxI)
