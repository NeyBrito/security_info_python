import socket
import sys #fornece a algumas variaveis direto do interpretador


def connectionsocket():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print('A conexão falhou')
        print('Erro: {}'.format(e))
        sys.exit()

    print("Socket criado com sucesso!")
    hostAlvo = input("Digite o Host ou IP a ser conectado: ")
    portaAlvo = input("Digite a porta a ser conectada: ")
    try:
        s.connect((hostAlvo, int(portaAlvo)))

        print("Cliente TCP conectado com sucesso no Host: " + hostAlvo + " e na porta: " + portaAlvo)
        s.shutdown(2)

    except socket.error as e:
        print("Não foi possivel conecta no Host: "+ hostAlvo + " e na porta: " + portaAlvo)
        print("Erro: ".format(e))
        sys.exit()


if __name__ == '__main__':
    connectionsocket()