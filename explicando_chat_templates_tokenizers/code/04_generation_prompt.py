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

tokenizer = AutoTokenizer.from_pretrained("HuggingFaceTB/SmolLM3-3B")

messages = [
    {"role": "user", "content": "Olá!"},
    {"role": "assistant", "content": "Prazer em conhecê-lo!"},
    {"role": "user", "content": "Posso fazer uma pergunta?"},
]

# SEM prompt de geração - para conversas completas
without_prompt = tokenizer.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=False
)

# COM prompt de geração - para inferência
with_prompt = tokenizer.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True
)

print("Sem generation prompt:")
print(without_prompt)
print("\n" + "=" * 50 + "\n")
print("Com generation prompt:")
print(with_prompt)
