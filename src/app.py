from server import Server

if __name__ == '__main__':
    server = Server(__name__)
    server.run(host='0.0.0.0', port=5000)

