# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a YouTube tutorial repository containing code examples and Slidev presentations in **Brazilian Portuguese**. Each subdirectory represents a different video tutorial with its own isolated setup, examples, and presentation materials.

YouTube Channel: https://www.youtube.com/@muri5511

## Repository Structure

The repository follows a flat structure where each tutorial is self-contained:

```
yt/
├── explicando_chat_templates_tokenizers/  # Chat templates & tokenizers tutorial
├── explicando_dataclasses_pydantic/       # Pydantic & dataclasses tutorial
└── explicando_uv/                         # uv package manager tutorial
```

Each tutorial directory contains:
- `slides.md` - Slidev presentation in Portuguese with voice-over notes in comments
- `code/` - Python example scripts demonstrating concepts
- `README.md` or `CLAUDE.md` - Tutorial-specific documentation
- `package.json` - Slidev dependencies (if presentations exist)

## Working with Slidev Presentations

All presentations use Slidev and are written in **Portuguese**.

### Running Presentations

From within a tutorial directory:

```bash
# Using Deno (preferred)
deno x @slidev/cli slides.md

# Using npx
npx @slidev/cli slides.md

# Using Bun
bunx @slidev/cli slides.md
```

### Presentation Characteristics
- Theme: `apple-basic` (common across presentations)
- Content: Full Portuguese with voice-over notes as markdown comments
- Code snippets: Often imported from external files in `code/` directory
- Addons: May include `slidev-addon-fancy-arrow`

## Working with Python Scripts

All Python examples use **inline script metadata (PEP 723)** for dependency management with `uv`.

### Running Python Scripts

```bash
# Execute a single script (uv creates environment automatically)
uv run code/01_exemplo.py

# From parent directory
uv run explicando_dataclasses_pydantic/code/01_exemplo.py
```

### Python Script Characteristics
- **Inline dependencies**: Scripts include `# /// script` metadata blocks
- **Python version**: Typically `>=3.10` or `>=3.13`
- **Code style**: English variable names, Portuguese comments
- **Credits**: Most include docstrings crediting source material
- **No shared environment**: Each script is self-contained

### Common Python Dependencies
- `transformers` - Hugging Face transformers library
- `pydantic` - Data validation
- `openai` - OpenAI API client
- `python-dotenv` - Environment variable management

## Project-Specific Details

### explicando_chat_templates_tokenizers
Based on Hugging Face Smol Course Unit 1.2. Contains 7 scripts demonstrating chat templates, tokenizers, multi-turn conversations, and generation prompts.

### explicando_dataclasses_pydantic
11 scripts progressing from basic type hints to advanced Pydantic features including custom validators, nested models, serialization, and LLM structured outputs.

Key file: `code/09_settings.py` uses `.env` file for configuration (present in directory).

### explicando_uv
Demonstrates uv package manager with:
- `pyproject.toml` - Project configuration
- `uv.lock` - Locked dependencies
- `.devcontainer/` - VS Code DevContainer setup

To work with this project:
```bash
uv sync      # Install dependencies
uv add pkg   # Add new dependency
```

## Language and Localization

- **Presentations**: Brazilian Portuguese
- **Code**: English identifiers, Portuguese comments
- **Documentation**: Portuguese
- **Commit messages**: Portuguese expected

## License

CC BY 4.0 (Creative Commons Attribution 4.0 International) - Users are free to share and adapt with proper attribution.
