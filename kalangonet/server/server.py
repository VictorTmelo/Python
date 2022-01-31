from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread
from handler import Handler

class KalangoServer(Thread):

  def __init__(self, host, port):
    Thread.__init__(self)
    self.host = host
    self.port = port
    self.stop = False

  def run(self):
    with socket(AF_INET, SOCK_STREAM) as s:
      s.bind((self.host, self.port))
      s.listen(1)

      while not self.stop:
        print('\nAguardando conexão...')
        conn, addr = s.accept()

        print(f'Conexão estabelecida com: {addr[0]}:{addr[1]}')
        handler = Handler(conn, addr)
        handler.start()