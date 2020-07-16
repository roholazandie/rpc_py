import os
import time
import wikipedia
import pymongo
from pymongo import MongoClient, IndexModel
from flask import Flask, make_response, jsonify
from xmlrpc.client import ServerProxy

PORT = 8080
proxy = ServerProxy('http://localhost:3000')


# def wiki_summary(title, sentences=2, chars=0, auto_suggest=True, redirect=False):
#     print("here")
#     return wikipedia.summary(title, sentences, chars, auto_suggest, redirect)


if __name__ == "__main__":
    print("Initiating Flask REST Service...")  
    app = Flask(__name__)  
    
    @app.route('/api/rest/v1.0/ask', methods=['POST'])
    def ask():
        response = make_response(jsonify({"response": proxy.wiki_summary("basketball")}))
        print("Wiki search of basketball: {}".format(response))    
        return None

    app.run(host='0.0.0.0', port=PORT, debug=True)