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
from transformers import pipeline

# Inicializar o pipeline
pipe = pipeline("text-generation", "HuggingFaceTB/SmolLM3-3B", device_map="auto")

# Definir a conversa
messages = [
    {
        "role": "system",
        "content": "Você é um assistente amigável que responde exclusivamente em português.",
    },
    {
        "role": "user",
        "content": "Qual foi a primeira capital do Brasil?",
    },
]

# Gerar resposta - pipeline gerencia templates automaticamente
response = pipe(messages, max_new_tokens=128, temperature=0.7)
print(response)
# endregion code
