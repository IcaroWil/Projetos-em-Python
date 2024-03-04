import socket

def portscan(ip):
    """
    Função para executar um scan de portas em um endereço IP específico.
    """
    print(f'\nIniciando varredura em {ip}')  # Exibe uma mensagem informando que a varredura de portas está sendo iniciada no endereço IP especificado.
    open_ports = 0  # Contador para registrar as portas abertas.

    # Iteração sobre a faixa de portas TCP (1 a 1024).
    for port in range(1, 1024):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria um novo socket TCP usando a API de baixo nível do Python.
        sock.settimeout(0.1)  # Define um tempo limite de conexão de 0,1 segundo para cada porta.

        try:
            result = sock.connect((ip, port))  # Tenta se conectar à porta no endereço IP especificado.
            if result == 0:  # Se a conexão for bem-sucedida (resultado = 0).
                print(f'Porta: {port} aberta')  # Exibe a porta aberta.
                open_ports += 1  # Incrementa o contador de portas abertas.

        except socket.error:
            pass  # Se ocorrer um erro durante a tentativa de conexão, ignora e continua o loop.

        finally:
            sock.close()  # Fecha o socket após a tentativa de conexão.

    print(f'{open_ports} portas abertas encontradas.')  # Exibe o número total de portas abertas.


portscan('Seu endereço IP')