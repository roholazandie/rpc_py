from xmlrpc.client import ServerProxy

proxy = ServerProxy('http://localhost:3000')

if __name__ == "__main__":
    print(proxy.do_some_dumb_task())