import random
from transformers import AutoTokenizer, GPT2LMHeadModel, pipeline

model_name = "sberbank-ai/rugpt3small_based_on_gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name).to("cpu")
tokenizer = AutoTokenizer.from_pretrained(model_name)
generation = pipeline("text-generation", model=model, tokenizer=tokenizer, device="cpu")

config = {
        "max_length": random.randint(200, 350),
        "temperature": 1.1,
        "top_p": 2.0,
        "num_beams": 10,
        "repetition_penalty": 1.5,
        "num_return_sequences": 9,
        "no_repeat_ngram_size": 2,
        "do_sample": True,
        }

def generate_res(response_) -> str:
    output = generation(response_, **config)[0]["generated_text"]
    return output
