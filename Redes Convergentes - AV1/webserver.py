import socket
import os
from threading import Thread
from email.utils import formatdate

class WebServer:

    def __init__(self, address='0.0.0.0', port=6789):
        self.port = port
        self.address = address

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((self.address, self.port))
            s.listen(10)

            while True:
                print('Waiting connections...')
                conn, addr = s.accept()
                req = HttpRequest(conn, addr)
                req.start()


class HttpRequest(Thread):

    def __init__(self, conn, addr):
        super(HttpRequest, self).__init__()
        self.conn = conn
        self.addr = addr
        self.CRLF = '\r\n'
        self.buffer_size = 4096
        self.file = ''
        self.fileType = ''
        self.fileLength = 0

    def run(self):

        request = self.conn.recv(self.buffer_size).decode()
        path = request.split('\r\n')[0].split(' ')[1]
        encontrado = False

        print(path)

        for filename in os.listdir("./public"):
            if '/' + filename == path:
                with open("./public/" + filename, "rb") as file:
                    self.file = file.read()
                    aux = filename.split(".")
                    self.fileType = aux[len(aux) - 1]
                    self.fileLength = self.file.__len__()
                    encontrado = True

        if path == '/':
            with open("./public/index.html", "rb") as file:
                self.file = file.read()
                self.fileType = "html"
                self.fileLength = self.file.__len__()
            encontrado = True

        if not encontrado:
            self.file = 'erro'

        # print(self.file)

        response = HttpResponse(self.conn, self.addr, self.file, self.fileType, self.fileLength)
        response.processRespose()

        self.conn.close()


class HttpResponse:

    def __init__(self, conn, addr, file, fileType, fileLength):
        self.conn = conn
        self.addr = addr
        self.file = file
        self.fileType = fileType
        self.fileLength = fileLength

    def processRespose(self):
        date = formatdate(timeval=None, localtime=False, usegmt=True)
        date = 'date: ' + date + '\r\n\r\n'

        if self.file == 'erro':
            statusLine = 'HTTP/1.0 404 Not Found\r\n'
            contentLength = 'Content-Length: 0\r\n'
            self.conn.sendall((statusLine + contentLength + date).encode())
        else:
            if self.fileType == "html":
                self.conn.sendall(f'HTTP/1.0 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\nContent-Length: {self.fileLength}\r\n{date}'.encode())
                self.conn.sendall(self.file)
            elif self.fileType == "js":
                self.conn.sendall(f'HTTP/1.0 200 OK\r\nContent-Type: text/javascript; charset=UTF-8\r\nContent-Length: {self.fileLength}\r\n{date}'.encode())
                self.conn.sendall(self.file)
            elif self.fileType == "png":
                self.conn.sendall(f'HTTP/1.0 200 OK\r\nContent-Type: image/png\r\nContent-Length: {self.fileLength}\r\n{date}'.encode())
                self.conn.sendall(self.file)
            elif self.fileType == "jpeg":
                self.conn.sendall(f'HTTP/1.0 200 OK\r\nContent-Type: image/jpeg\r\nContent-Length: {self.fileLength}\r\n{date}'.encode())
                self.conn.sendall(self.file)