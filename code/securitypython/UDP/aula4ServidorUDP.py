import socket


class ServidorUDP:
     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
     print('Socket criado com sucesso.')
     host = 'localhost'
     porta = 5432

     s.bind((host, porta))
     mensagem = "\nServidor: Oláaa cliente. Ta tranquilo e ai?"

     while 1:
         dados, end = s.recvfrom(4096)
         if dados:
             print("Servidor enviando mensagem...")
             s.sendto(dados + (mensagem.encode()), end)

if __name__ == '__main__':
    servidor = ServidorUDP
    servidor()