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

tokenizer = AutoTokenizer.from_pretrained("HuggingFaceTB/SmolLM3-3B")

# Saída estruturada em JSON
json_messages = [
    {"role": "user", "content": "Formate a resposta em JSON"},
    {"role": "assistant", "content": '{"name": "'},
]

# Continuar a mensagem final (prefill)
continue_mode = tokenizer.apply_chat_template(
    json_messages, tokenize=False, continue_final_message=True
)

# Começar nova mensagem
new_message = tokenizer.apply_chat_template(
    json_messages, tokenize=False, add_generation_prompt=True
)

print("Continuando mensagem final:")
print(continue_mode)
print("\n" + "=" * 50 + "\n")
print("Iniciando nova mensagem:")
print(new_message)
# endregion code
