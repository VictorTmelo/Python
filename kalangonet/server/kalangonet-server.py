from server import KalangoServer

if __name__ == '__main__':

  print('Inicializando o KalangoNet Server...')

  server = KalangoServer('localhost', 50005)
  server.start()

