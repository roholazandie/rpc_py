from xmlrpc.client import ServerProxy

proxy = ServerProxy('http://localhost:3000')

if __name__ == "__main__":
    print(proxy.list_directory('/'))

    print("3 is even: {}".format(proxy.is_even(3)))
    print("100 is even: {}".format(proxy.is_even(100)))