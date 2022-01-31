import socket
import threading

# Detalhe -> IP e porta do cliente podem mudar

host = 'localhost'
port = 12321

def handle_connection(s):

    while True:
        data = s.recv(1024)

        msg = data.decode('utf8')

        print(f"Recebido: {msg}", end="")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # Se conecta ao servidor
    s.connect((host,port))

    t = threading.Thread(target=handle_connection, args=(s,))
    t.start()

    while True:

        print("> ", end="")
        msg = input()
        msg += "\r\n"

        # Envia ao servidor
        s.sendall(msg.encode('utf8'))


