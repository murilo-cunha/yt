# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///

"""
Baseado em: Hugging Face Smol Course - Unit 1.2
https://huggingface.co/learn/smol-course/unit1/2
"""

# region code
# Modo padrão - resposta direta
standard_messages = [
    {"role": "user", "content": "Quanto é 15 × 24?"},
    {"role": "assistant", "content": "15 × 24 = 360"},
]

# Modo thinking - mostra raciocínio
thinking_messages = [
    {"role": "user", "content": "Quanto é 15 × 24?"},
    {
        "role": "assistant",
        "content": "<|thinking|>\nPreciso multiplicar 15 por 24. Vou quebrar isso:\n15 × 24 = 15 × (20 + 4) = (15 × 20) + (15 × 4) = 300 + 60 = 360\n</|thinking|>\n\n15 × 24 = 360",
    },
]

# O modo thinking permite que o modelo mostre seu raciocínio
# Útil para tarefas complexas que requerem explicação passo a passo
# endregion code
