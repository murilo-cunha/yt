# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///

"""
Baseado em: Hugging Face Smol Course - Unit 1.2
https://huggingface.co/learn/smol-course/unit1/2
"""

# Mensagem de sistema para assistente profissional
professional_system = {
    "role": "system",
    "content": "Você é um agente de atendimento ao cliente profissional. Seja sempre educado, claro e prestativo.",
}

# Mensagem de sistema para especialista técnico
technical_system = {
    "role": "system",
    "content": "Você é um engenheiro de software sênior. Forneça explicações técnicas detalhadas com exemplos de código quando apropriado.",
}

# Mensagem de sistema para assistente criativo
creative_system = {
    "role": "system",
    "content": "Você é um assistente de escrita criativa. Ajude os usuários a criar histórias envolventes.",
}

# Mensagens de sistema definem o comportamento do modelo
# São a primeira mensagem e influenciam toda a conversa
