import torch
import numpy as np
from transformers import (RobertaTokenizer, RobertaForSequenceClassification, InputExample,
                          glue_convert_examples_to_features, pipeline)

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

    def similarity_with_concept(self, text, concept):
        example = InputExample(guid='0', text_a=text, text_b=concept)
        feature = glue_convert_examples_to_features(examples=[example],
                                                    tokenizer=self.tokenizer,
                                                    max_length=128,
                                                    output_mode='regression',
                                                    label_list=[None])

        input_ids = torch.tensor(feature[0].input_ids).unsqueeze(0)
        attention_mask = torch.tensor(feature[0].attention_mask).unsqueeze(0)

        with torch.no_grad():
            outputs = self.model(input_ids=input_ids, attention_mask=attention_mask)

        return outputs[0].item()

    def similarity_with_concepts(self, text, concepts):
        examples = [InputExample(guid='0', text_a=text, text_b=concept) for concept in concepts]
        features = glue_convert_examples_to_features(examples=examples,
                                                     tokenizer=self.tokenizer,
                                                     max_length=128,
                                                     output_mode='regression',
                                                     label_list=[None])

        input_ids = torch.tensor([feature.input_ids for feature in features])
        attention_mask = torch.tensor([feature.attention_mask for feature in features])

        with torch.no_grad():
            outputs = self.model(input_ids=input_ids, attention_mask=attention_mask)
            outputs = outputs[0].T.tolist()[0]

        return outputs

class Summarization:
    def __init__(self):
        pass

if __name__ == "__main__":
    try:
        tokenizer = RobertaTokenizer.from_pretrained('/home/rohola/codes/program-r/libs/pretrain_roberta_model')
        model = RobertaForSequenceClassification.from_pretrained('/home/rohola/codes/program-r/libs/pretrain_roberta_model')

        sentence1 = "Dogs are cute."
        sentence2 = "I need an Macbook."
        sentence3 = "Computer technology is awesome."

        example = InputExample(guid=0, text_a=sentence3, text_b=sentence2, label=0)
        feature = glue_convert_examples_to_features(examples=[example],
                                                    tokenizer=tokenizer,
                                                    max_length=128,
                                                    output_mode='regression',
                                                    label_list=[None])

        input_ids = torch.tensor(feature[0].input_ids).unsqueeze(0)
        attention_mask = torch.tensor(feature[0].attention_mask).unsqueeze(0)

        with torch.no_grad():
            outputs = model(input_ids=input_ids, attention_mask=attention_mask)
            print("model outputs: {}".format(outputs[0].item()))
            
        semantic_similarity = SemanticClassifer(model, tokenizer)
        s1 = semantic_similarity.similarity_with_concept("The computer technology is awesome", "Intel")
        s2 = semantic_similarity.similarity_with_concept("The computer technology is awesome", "dog")
        print("semantics similarity scores: {}, {}".format(s1, s2))

        ss = semantic_similarity.similarity_with_concepts("The computer technology is awesome",
                                                        ["dogs", "peperoni", "Intel"])
        print("semantics similarity scores: {}".format(ss))
    except KeyboardInterrupt:
        print("Exiting")