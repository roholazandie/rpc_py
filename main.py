from xmlrpc.server import SimpleXMLRPCServer
import os

server = SimpleXMLRPCServer(('localhost', 3000), logRequests=True)

def list_directory(dir):
    return os.listdir(dir)

server.register_function(list_directory)

if __name__ == "__main__":
    try:
        print('Serving...')
        server.serve_forever()
    except KeyboardInterrupt:
        print("Exiting")