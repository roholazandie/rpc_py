from xmlrpc.server import SimpleXMLRPCServer
import os
import time

server = SimpleXMLRPCServer(('localhost', 3000), logRequests=True)

def list_directory(dir):
    return os.listdir(dir)

def do_some_dumb_task():
    time.sleep(5)
    return "done"

server.register_function(list_directory)
server.register_function(do_some_dumb_task)

if __name__ == "__main__":
    try:
        print('Serving...')
        server.serve_forever()
    except KeyboardInterrupt:
        print("Exiting")