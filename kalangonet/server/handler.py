import json

from models import User
from threading import Thread

class Handler(Thread):
  
  def __init__(self, conn, addr):
    Thread.__init__(self)
    self.conn = conn
    self.addr = addr

  def run(self):
    with self.conn:
      while True:
        print(f'Aguardando comando de {self.addr[0]}:{self.addr[1]}')
        data = self.conn.recv(1024)
        if not data: break
        
        request = json.loads(data.decode('utf8'))

        if request['action'] == 'create_user':
          file = open('c:\Desenvolvimento\Workspaces\PYTHON\kalangonet\server\database.json', 'r')
          content = file.read()
          file.close()
          db = json.loads(content)

          user = User(request['data']['name'], request['data']['email'], request['data']['password'])

          db['users'].append(user.map())          

          content = json.dumps(db)
          file = open('c:\Desenvolvimento\Workspaces\PYTHON\kalangonet\server\database.json', 'w')
          file.write(content)
          file.close()

        else:
          self.conn.sendall("Invalid command".encode('utf8'))

        