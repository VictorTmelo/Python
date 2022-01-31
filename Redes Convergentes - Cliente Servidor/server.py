import socket

# Detalhe -> IP e porta do servidor são sempre fixas

# Qualquer endereçco IP
host = ""

port = 12321
# 0 ... 65535
# Portas Publicas -> 0 ... 1024
# HTTP -> 80
# DNS -> 53


# IPv4 e TCP
# Atribuindo servidor a variavel s
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # Vinclunado no servidor endereço e porta que irão receber conexões
    s.bind((host,port))

    # Quantas conexões pendentes podem ficar em fila
    s.listen(1)

    print("Aguardando Conexões...")
    conn, addr = s.accept()
    # conn = objeto que representa a conexão entre o cliente e o servidor
    # addr = objeto com informações sobre a conexão

    with conn:

        print(f"Conexão Estabelecida com {addr}")

        while True:

            # Recebe os dados do cliente -> Array de até 1024 bytes
            data = conn.recv(1024)

            msg = data.decode('utf8')

            if not data: break
            #if msg == "EOF\r\n: break

            print(f"Recebido: {msg}")

            # Retorna os dados para o cliente
            conn.sendall(data)

