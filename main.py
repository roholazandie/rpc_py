import os
import time
import requests
import wikipedia
import numpy as np
from flask import Flask, make_response, jsonify
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification, TextClassificationPipeline
from xmlrpc.server import SimpleXMLRPCServer
from sentiment_classifier import SentimentClassifer
from newsapi import NewsApiClient
from pyowm import OWM

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

def get_news(sources=None, country=None):
    try:
        url = "https://microsoft-azure-bing-news-search-v1.p.rapidapi.com/"

        headers = {
            'x-rapidapi-host': "microsoft-azure-bing-news-search-v1.p.rapidapi.com",
            'x-rapidapi-key': "2d82bb5d95msh2a4e5c2a45a8eb3p18b00ejsn98308d90b548"
            }
            
        response = requests.request("GET", url=url, headers=headers, params=None)
        headline_dict = response.json()
        headline = headline_dict['value'][0]['name']
        return headline
    except Exception as ex:
        print("error getting request. {}".format(ex))
        return ""

def get_weather():
    api_key = 'b42dab02ba31304c08ae33bd9c63d0a4'
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
        print('Serving...')
        register_functions(server)
        server.serve_forever()
    except KeyboardInterrupt:
        print("Exiting")