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

from transformers import pipeline

# Inicializar o pipeline
pipe = pipeline("text-generation", "HuggingFaceTB/SmolLM3-3B", device_map="auto")

# Definir a conversa
messages = [
    {
        "role": "system",
        "content": "Você é um assistente amigável que sempre responde como um pirata",
    },
    {
        "role": "user",
        "content": "Quantos helicópteros um humano pode comer de uma vez?",
    },
]

# Gerar resposta - pipeline gerencia templates automaticamente
response = pipe(messages, max_new_tokens=128, temperature=0.7)
print(response[0]["generated_text"][-1])
