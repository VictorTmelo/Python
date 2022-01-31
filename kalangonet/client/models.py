import bcrypt
import json

class User:

  def __init__(self, name, email, password):
    self.name = name
    self.email = email
    self.password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

  def verifyPassword(self, password):
    return bcrypt.checkpw(password.encode('utf8'), self.senha)

  def map(self):
    map = {'name': self.name, 'email': self.email, 'password': self.password.decode('utf8')}
    return map

class Request:

  def __init__(self, action, data):
    self.action = action
    self.data = data

  def get_json(self):
    req = {'action': self.action, 'data': self.data}
    return json.dumps(req)

class CreateUserRequest(Request):

  def __init__(self, data):
      super().__init__('create_user', data)