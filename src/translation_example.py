from transformers import AutoTokenizer, AutoModelWithLMHead, pipeline

tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-de-en")
model = AutoModelWithLMHead.from_pretrained("Helsinki-NLP/opus-mt-de-en")

en_to_de_translator = pipeline("translation_en_to_de")
german_text = en_to_de_translator("Hugging Face is a technology company based in New York and Paris", max_length=40)
print(german_text)

# NOTE: pipeline does not exist
# de_to_en_translator = pipeline("translation_de_to_en")
# english_text = de_to_en_translator(german_text, max_length=40)
# print(english_text)