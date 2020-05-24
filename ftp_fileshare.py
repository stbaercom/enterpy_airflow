import os


from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def main():
    authorizer = DummyAuthorizer()
    fp = os.path.join(os.path.dirname(__file__),"data/ftp")
    authorizer.add_user('ftp', 'ftp', fp, perm='elradfmwMT')

    handler = FTPHandler
    handler.authorizer = authorizer

    address = ('', 2121)
    server = FTPServer(address, handler)
    server.serve_forever()

if __name__ == '__main__':
    main()