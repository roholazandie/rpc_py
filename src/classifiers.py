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

class SemanticClassifer:

    def __init__(self, model, tokenizer):
        self.model = model
        self.tokenizer = tokenizer

    def __call__(self, text1, text2):
        # encoded_input1 = self.tokenizer(text1, return_tensors='pt')
        # output1 = self.model(**encoded_input1)

        # encoded_input2 = self.tokenizer(text2, return_tensors='pt')
        # output2 = self.model(**encoded_input2)

        # similarity_score = np.inner(encoded_input1, encoded_input2)[0][0]



        input_ids1 = torch.tensor(self.tokenizer.encode(text1)).unsqueeze(0)
        outputs1 = self.model(input_ids1)
        last_hidden_states1 = outputs1[0].detach().numpy()  # The last hidden-state is the first element of the output tuple

        input_ids2 = torch.tensor(self.tokenizer.encode(text2)).unsqueeze(0)
        outputs2 = self.model(input_ids2)
        last_hidden_states2 = outputs2[0].detach().numpy()  # The last hidden-state is the first element of the output tuple

        similarity_score = np.inner(last_hidden_states2, last_hidden_states1)[0][0]
        return similarity_score