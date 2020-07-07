import os
import time
import wikipedia

from xmlrpc.server import SimpleXMLRPCServer

server = SimpleXMLRPCServer(('localhost', 3000), logRequests=True)

def list_directory(dir):
    return os.listdir(dir)

def do_some_dumb_task():
    time.sleep(5)
    return "done"

def is_even(n):
    return n % 2 == 0

def hello_world():
    print("hello world")

def wiki_summary(title, sentences=2, chars=0, auto_suggest=True, redirect=False):
    return wikipedia.summary(title, sentences, chars, auto_suggest, redirect)

server.register_function(list_directory)
server.register_function(is_even)
server.register_function(hello_world)
server.register_function(wiki_summary)

if __name__ == "__main__":
    try:
        print('Serving...')
        server.serve_forever()
    except KeyboardInterrupt:
        print("Exiting")