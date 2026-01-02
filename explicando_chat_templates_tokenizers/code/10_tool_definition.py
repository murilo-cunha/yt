# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
"""
Baseado em: Hugging Face Smol Course - Unit 1.2
https://huggingface.co/learn/smol-course/unit1/2
"""

# region code
# Definição de ferramentas segue o formato JSON Schema

weather_tool = {
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
            "required": ["location"],  # Parâmetros obrigatórios
        },
    },
}

calculator_tool = {
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
}

# Lista de ferramentas disponíveis
tools = [weather_tool, calculator_tool]
# endregion code
