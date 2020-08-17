import requests
import time

for sentence in ["I want a MacBook.", "This country music is old style."]:
    for concept in ["music", "computers"]:
        r = requests.post('http://localhost:8080/similarity_concept',  json={'concept': concept, "text": sentence})
        print(f"{concept} and {sentence} similarity is: {r.text}")