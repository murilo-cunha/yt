# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "transformers>=4.46.0",
#     "torch>=2.0.0",
#     "accelerate>=1.12.0",
# ]
# ///

"""
Baseado em: Hugging Face Smol Course - Unit 1.2
https://huggingface.co/learn/smol-course/unit1/2
"""

# region code
from transformers import AutoTokenizer

# Carregar tokenizer do SmolLM3
tokenizer = AutoTokenizer.from_pretrained("HuggingFaceTB/SmolLM3-3B")

messages = [
    {"role": "system", "content": "Você é um assistente técnico."},
    {"role": "user", "content": "Explique o que é um chat template?"},
    {
        "role": "assistant",
        "content": "Eles padronizam a conversão de diálogos em um formato de texto que LLMs consiguem entender e processar corretamente.",
    },
    {"role": "user", "content": "Como é esse formato?"},
]

# Aplicar o chat template
formatted_chat = tokenizer.apply_chat_template(
    messages,
    tokenize=False,  # Retornar string em vez de tokens
    add_generation_prompt=True,  # Adicionar prompt para próxima resposta
)

print(formatted_chat)
# endregion code
