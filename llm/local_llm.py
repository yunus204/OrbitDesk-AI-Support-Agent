import torch
from transformers import AutoTokenizer, AutoModelForCausalLM


class LocalLLM:

    def __init__(self):

        model_name = "Qwen/Qwen2.5-1.5B-Instruct"

        print("Loading Qwen2.5-1.5B-Instruct...")

        self.tokenizer = AutoTokenizer.from_pretrained(
            model_name,
            trust_remote_code=True
        )

        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float32,
            device_map="cpu"
        )

    def generate(self, prompt: str) -> str:

        messages = [
            {
                "role": "system",
                "content": (
                    "You are OrbitDesk AI Support Assistant.\n"
                    "Answer ONLY using the provided context.\n"
                    "If the answer is not present in the context, reply exactly:\n"
                    "'I couldn't find that information in the knowledge base.'"
                ),
            },
            {
                "role": "user",
                "content": prompt,
            },
        ]

        text = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True,
        )

        inputs = self.tokenizer(
            text,
            return_tensors="pt"
        )

        outputs = self.model.generate(
            **inputs,
            max_new_tokens=150,
            do_sample=False,
            pad_token_id=self.tokenizer.eos_token_id,
        )

        response = outputs[0][inputs.input_ids.shape[1]:]

        return self.tokenizer.decode(
            response,
            skip_special_tokens=True
        ).strip()