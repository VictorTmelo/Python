from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread
from models import User, CreateUserRequest


class KalangoClient(Thread):

  def __init__(self, host, port):
    Thread.__init__(self)
    self.host = host
    self.port = port

  def run(self):
    with socket(AF_INET, SOCK_STREAM) as s:
      print(f'Realizando conexão com {self.host}:{self.port}')
      s.connect((self.host, self.port))

      print('Conexão estabelecida')
      while True:
        cmd = input('> ')

        if cmd.startswith('create'):
          json = self.get_user_json(cmd)
          s.sendall(json.encode('utf8'))
          #data = s.recv(1024)
          #print(f'{data.decode("utf8")}')

        elif cmd.startswith('add'):
          ...

        elif cmd.startswith('quit'):
          s.close()
          break
        else:
          print('Comando inválido')

  def get_user_json(self, cmd):
    aux = cmd.split(' ')
    if aux[1].startswith('user') and len(aux) == 5:
      usuario = User(aux[2], aux[3], aux[4])
      req = CreateUserRequest(usuario.map())
      return req.get_json()


