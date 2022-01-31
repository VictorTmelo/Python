import socket

# Detalhe -> IP e porta do cliente podem mudar

host = 'localhost'
port = 12321

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # Se conecta ao servidor
    s.connect((host,port))

    # Envia ao servidor
    s.sendall("Hello World". encode('utf8'))

    data = s.recv(1024)

    msg = data.decode('utf8')

    print(f"Recebido: {msg}")