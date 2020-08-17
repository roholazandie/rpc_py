#import xmlrpclib
from xmlrpc.client import ServerProxy


server = ServerProxy('http://localhost:3000')


print(server.get_semantic_similarity("I want a MacBook.", "computers"))
print(server.get_semantic_similarity("I want a MacBook.", "music"))
print(server.get_semantic_similarity("You like Elvis!", "computers"))
print(server.get_semantic_similarity("You like Elvis!", "music"))
