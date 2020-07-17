import requests
import time

for sentence in ["I love you.", "I hate you", "no", "I am having fun", "i feel sad.", "what is the meaning of life.", "what should we talk about?"]:
    r = requests.post('http://localhost:8080/sentiment',  json={'question': sentence})
    print(r.text)