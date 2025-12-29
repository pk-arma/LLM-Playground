from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

MODEL_NAME = "distilgpt2"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

device = "mps" if torch.backends.mps.is_available() else "cpu"
model.to(device)

def generate_text(prompt: str, max_tokens: int, temperature: float):
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    output = model.generate(
        **inputs,
        max_new_tokens=max_tokens,
        temperature=temperature,
        do_sample=True
    )
    return tokenizer.decode(output[0], skip_special_tokens=True)
