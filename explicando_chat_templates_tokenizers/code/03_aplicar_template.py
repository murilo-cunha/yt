# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "transformers>=4.46.0",
# ]
# ///

"""
Baseado em: Hugging Face Smol Course - Unit 1.2
https://huggingface.co/learn/smol-course/unit1/2
"""

from transformers import AutoTokenizer

# Carregar tokenizer do SmolLM3
tokenizer = AutoTokenizer.from_pretrained("HuggingFaceTB/SmolLM3-3B")

messages = [
    {"role": "system", "content": "Você é um assistente técnico."},
    {"role": "user", "content": "Explique o que é um chat template?"},
]

# Aplicar o chat template
formatted_chat = tokenizer.apply_chat_template(
    messages,
    tokenize=False,  # Retornar string em vez de tokens
    add_generation_prompt=True,  # Adicionar prompt para próxima resposta
)

print(formatted_chat)
