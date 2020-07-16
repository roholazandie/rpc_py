import os
import time
import wikipedia
import pymongo
from pymongo import MongoClient, IndexModel
from flask import Flask, make_response, jsonify

from xmlrpc.server import SimpleXMLRPCServer

server = SimpleXMLRPCServer(('localhost', 3000), logRequests=True)

def list_directory(dir):
    return os.listdir(dir)

def is_even(n):
    return n % 2 == 0

def hello_world():
    print("hello world")

def wiki_summary(title, sentences=2, chars=0, auto_suggest=True, redirect=False):
    return wikipedia.summary(title, sentences, chars, auto_suggest, redirect)

def load_client_properties(self, db, userid):
    try:
        if db['user_info'].find_one({'userid': userid}) is not None:
            # print("Found user")
            user_info = self.db['user_info'].find_one({'userid': userid})
            print("user name: {}".format(user_info['name']))
            print("user location: {}".format(user_info['location']))
            print("user time zone: {}".format(user_info['time zone']))
            # self.user_name = user_info['name']
            # self.location = user_info['location']
            # self.time_zone = user_info['time zone']
        else:
            print("userid {} in database not found".format(userid))
            # document = {
            #     "userid": userid,
            #     "name": "Uknown",
            #     "location": "Uknown", 
            #     "time zone": "Uknown"
            # }
    except Exception as e:
        print("Exception caught loading properties")

def flask_app():
    print("Initiating Flask REST Service...")  
    app = Flask(__name__)  
    
    @app.route('/api/rest/v1.0/ask', methods=['POST'])
    def ask():
        response = make_response(jsonify({"response": proxy.wiki_summary("basketball")}))
        print("Wiki search of basketball: {}".format(response))    
        return None

    app.run(host='0.0.0.0', port=PORT, debug=True)

def register_functions(server):
    server.register_function(list_directory)
    server.register_function(is_even)
    server.register_function(hello_world)
    server.register_function(wiki_summary)
    server.register_function(flask_app)

if __name__ == "__main__":
    try:
        print('Serving...')
        register_functions(server)
        server.serve_forever()
    except KeyboardInterrupt:
        print("Exiting")