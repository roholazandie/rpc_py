import os
import time
import wikipedia
import pymongo
from pymongo import MongoClient, IndexModel
from flask import Flask
from xmlrpc.server import SimpleXMLRPCServer

PORT = 8080
app = Flask(__name__)
server = SimpleXMLRPCServer(('localhost', 3000), logRequests=True)


def wiki_summary(title, sentences=2, chars=0, auto_suggest=True, redirect=False):
    print("here")
    return wikipedia.summary(title, sentences, chars, auto_suggest, redirect)

if __name__ == "__main__":
    print("Initiating Flask REST Service...")    
    app.run(host='0.0.0.0', port=PORT, debug=True)

    server.register_function(wiki_summary)
    print("Initiating XMLRPCSever...")
    server.serve_forever()