import os
import time
import requests
import wikipedia
import numpy as np
from flask import Flask, make_response, jsonify
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification, RobertaTokenizer, RobertaTokenizerFast, RobertaForSequenceClassification
from xmlrpc.server import SimpleXMLRPCServer
from classifiers import SentimentClassifer, SemanticClassifer
from newsapi import NewsApiClient
from pyowm import OWM
import yaml
from yaml import load, dump

server = SimpleXMLRPCServer(('localhost', 3000), logRequests=True)

def list_directory(dir):
    return os.listdir(dir)

def is_even(n):
    return n % 2 == 0

def hello_world():
    print("hello world")

def wiki_summary(title, sentences=2, chars=0, auto_suggest=True, redirect=False):
    try:
        return wikipedia.summary(title, sentences, chars, auto_suggest, redirect)
    except:
        return "No result"

def check_sentiment(text):
    tokenizer = DistilBertTokenizer.from_pretrained('./pretrain_distillbert_full_sst')
    model = DistilBertForSequenceClassification.from_pretrained('./pretrain_distillbert_full_sst')
    sentiment_classifier = SentimentClassifer(model, tokenizer)
    result = sentiment_classifier(text)
    sentiment = max(result, key=result.get)
    sentiment_distribution = list(result.values())
    print("sentiment of {}: {}".format(text, sentiment))
    return sentiment

def get_semantic_similarity(text1, text2):
    model = RobertaForSequenceClassification.from_pretrained('./pretrain_roberta_model')
    print("model created...")

    # NOTE: This is throwing an error with the bos token
    # tokenizer = RobertaTokenizer.from_pretrained('./pretrain_roberta_model')

    tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
    print("tokenizer created...")

    semantic_similarity_classifier = SemanticClassifer(model, tokenizer)
    result = semantic_similarity_classifier(text1, text2)
    print("similarity score: {}".format(result))
    return result

def get_news(sources=None, country=None):
    try:
        with open("./src/api_key_config.yaml", 'r') as stream:
            data = yaml.safe_load(stream)
            headers = data['news']['headers']
            url = data['news']['url']
            
            response = requests.request("GET", url=url, headers=headers, params=None)
            headline_dict = response.json()
            headline = headline_dict['value'][0]['name']
            return headline
    except Exception as ex:
        print("error getting request. {}".format(ex))
        return ""

def get_weather():
    with open("./src/api_key_config.yaml", 'r') as stream:
        data = yaml.safe_load(stream)
        api_key = data['weather']
        location = "Denver, USA"
        observation = OWM(api_key).weather_at_place(location)
        weather = observation.get_weather()
        return str(weather.get_temperature(unit='fahrenheit')['temp'])

def register_functions(server):
    server.register_function(list_directory)
    server.register_function(is_even)
    server.register_function(hello_world)
    server.register_function(wiki_summary)
    server.register_function(check_sentiment)
    server.register_function(get_news)
    server.register_function(get_weather)

if __name__ == "__main__":
    try:
        # print('Serving...')
        # register_functions(server)
        # server.serve_forever()

        text1 = "I like playing basketball."
        text2 = "I like watching the NBA."
        text3 = "Ice cream is the best!"

        get_semantic_similarity(text1, text2)
        get_semantic_similarity(text1, text3)
        get_semantic_similarity(text1, text1)
    except KeyboardInterrupt:
        print("Exiting")