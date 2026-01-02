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

from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("HuggingFaceTB/SmolLM3-3B")

# Definir ferramentas disponíveis
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Obter clima atual de uma localização",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "Cidade e estado, ex: São Paulo, SP",
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": "Unidade de temperatura",
                    },
                },
                "required": ["location"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Realizar cálculos matemáticos",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Expressão matemática para avaliar",
                    }
                },
                "required": ["expression"],
            },
        },
    },
]

# region code

# `tools` definidas acima

# Conversa com uso de ferramentas
messages = [
    {"role": "system", "content": "Você é um assistente com acesso a ferramentas."},
    {"role": "user", "content": "Como está o clima em Paris?"},
    {
        "role": "assistant",
        "content": "Vou verificar o clima em Paris para você.",
        "tool_calls": [
            {
                "id": "call_1",
                "type": "function",
                "function": {
                    "name": "get_weather",
                    "arguments": '{"location": "Paris, France", "unit": "celsius"}',
                },
            }
        ],
    },
    {
        "role": "tool",
        "tool_call_id": "call_1",
        "content": '{"temperature": 22, "condition": "sunny", "humidity": 60}',
    },
    {
        "role": "assistant",
        "content": "O clima em Paris está ensolarado com 22°C e 60% de umidade. Um belo dia!",
    },
]

# Aplicar chat template com ferramentas
formatted_with_tools = tokenizer.apply_chat_template(
    messages, tools=tools, tokenize=False, add_generation_prompt=False
)

print("Chat template com ferramentas:")
print(formatted_with_tools)
# endregion code
