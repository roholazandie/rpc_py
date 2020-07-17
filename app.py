import os
import time
import wikipedia
#import pymongo
#from pymongo import MongoClient, IndexModel
from flask import Flask, make_response, jsonify, request
from xmlrpc.client import ServerProxy

PORT = 8080
proxy = ServerProxy('http://localhost:3000')

if __name__ == "__main__":
    print("Initiating Flask REST Service...")  
    app = Flask(__name__)
    
    @app.route('/wiki', methods=['POST'])
    def ask_wiki():
        r = request.get_json()
        print(r)
        response = make_response(jsonify({"response": proxy.wiki_summary(r["question"])}))
        return response


    @app.route('/list_directory', methods=['POST'])
    def ask_dir():
        response = make_response(jsonify({"response": proxy.list_directory('/')}))
        return response


    @app.route('/is_even', methods=['POST'])
    def ask_even():
        response = make_response(jsonify({"response": proxy.is_even(4)}))
        return response

    app.run(host='127.0.0.1', port=PORT, threaded=True)



#curl --header "Content-Type: application/json" --request POST --data '{"question":"basketball"}' http://localhost:8080/wiki
