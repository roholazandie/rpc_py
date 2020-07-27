import os
import time
import wikipedia
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

    @app.route('/sentiment', methods=['POST'])
    def ask_sentiment():
        r = request.get_json()
        response = make_response(jsonify({"response": proxy.check_sentiment(r["question"])}))
        return response

    @app.route('/similarity', methods=['POST'])
    def ask_similarity():
        r = request.get_json()
        response = make_response(jsonify({"response": proxy.get_semantic_similarity(r['text'], r['concept'])}))
        return response

    @app.route('/news', methods=['POST'])
    def ask_news():
        r = request.get_json()
        response = make_response(jsonify({"response": proxy.get_news()}))
        return response

    @app.route('/weather', methods=['POST'])
    def ask_weather():
        r = request.get_json()
        response = make_response(jsonify({"response": proxy.get_weather()}))
        return response

    app.run(host='127.0.0.1', port=PORT, threaded=True)



#curl --header "Content-Type: application/json" --request POST --data '{"question":"basketball"}' http://localhost:8080/wiki
