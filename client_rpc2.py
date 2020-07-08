from xmlrpc.client import ServerProxy

proxy = ServerProxy('http://localhost:3000')

if __name__ == "__main__":
    print("Wiki search of basketball: {}".format(proxy.wiki_summary("basketball")))