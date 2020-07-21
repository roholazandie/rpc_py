import torch
import numpy as np

class SentimentClassifer:

    def __init__(self, model, tokenizer):
        self.model = model
        self.tokenizer = tokenizer

    def __call__(self, text):
        input_ids = torch.tensor(self.tokenizer.encode(text, add_special_tokens=True)).unsqueeze(0)
        outputs = self.model(input_ids)
        outputs = outputs[0].detach().numpy()
        scores = np.exp(outputs) / np.exp(outputs).sum(-1)
        scores = scores[0].tolist()
        result = {"negative": scores[0], "neutral": scores[1], "positive": scores[2]}
        return result