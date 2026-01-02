# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///

"""
Baseado em: Hugging Face Smol Course - Unit 1.2
https://huggingface.co/learn/smol-course/unit1/2
"""

# region code
# Estrutura básica de mensagens
messages = [
    {
        "role": "system",
        "content": "Você é um assistente técnico focado em programação.",
    },
    {"role": "user", "content": "O que são chat templates?"},
    {
        "role": "assistant",
        "content": "Chat templates estruturam conversas entre usuários e modelos de IA...",
    },
]

# Cada mensagem tem:
# - role: identifica quem está falando
# - content: o conteúdo da mensagem
# endregion code
