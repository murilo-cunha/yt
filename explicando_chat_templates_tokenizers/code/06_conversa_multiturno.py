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

pipe = pipeline("text-generation", "HuggingFaceTB/SmolLM3-3B", device_map="auto")

# Configurar parâmetros de geração
generation_config = {
    "max_new_tokens": 200,
    "temperature": 0.8,
    "do_sample": True,
    "top_p": 0.9,
}

# Conversa multi-turno
conversation = [
    {"role": "system", "content": "Você é um tutor de matemática."},
    {"role": "user", "content": "Pode me ajudar com cálculo?"},
]

# Gerar primeira resposta
response = pipe(conversation, **generation_config)
conversation = response[0]["generated_text"]

# Continuar a conversa
conversation.append({"role": "user", "content": "O que é uma derivada?"})
response = pipe(conversation, **generation_config)

# Imprimir conversa final
for message in response[0]["generated_text"]:
    print(f"{message['role']}: {message['content']}")
