from client import KalangoClient

if __name__ == '__main__':
  print('Inicializando o KalangoNet Client...')

  client = KalangoClient('localhost', 50005)
  client.start()


