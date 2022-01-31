import socket
import threading

# Detalhe -> IP e porta do servidor são sempre fixas

# Qualquer endereçco IP
host = ""

# 0 ... 65535
# Portas Publicas -> 0 ... 1024
port = 12321

clients = []

def handle_connection(conn, addr):

    with conn:

        print(f"Conexão Estabelecida com {addr}")

        while True:

            # Recebe os dados do cliente -> Array de até 1024 bytes
            data = conn.recv(1024)

            msg = data.decode('utf8')

            # if not data: break
            if msg == "EOC\r\n": break

            print(f"Recebido: {msg}", end="")

            # Retorna os dados para o cliente
            conn.sendall(data)

            # Chat entre clientes
            '''for c in clients:
                if c != conn:
                    c.sendall(data)'''


# IPv4 e TCP
# Atribuindo servidor a variavel s
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # Vinclunado no servidor endereço e porta que irão receber conexões
    s.bind((host,port))

    # Quantas conexões pendentes podem ficar em fila
    s.listen(1)

    while True:
        print("Aguardando Conexões...")
        conn, addr = s.accept()
        # conn = objeto que representa a conexão entre o cliente e o servidor
        # addr = objeto com informações sobre a conexão

        clients.append(conn)

        t = threading.Thread(target=handle_connection, args=(conn,addr,))
        t.start()



