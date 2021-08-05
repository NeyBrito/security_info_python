import os #Integra Programas e recursos do Sistema Operacional

class Ping():
    def pingar(self):
        print('#' * 60)
        #Variável que irá receber o ip/host do usuário
        ip_ou_host = input("Digite IP ou Host a ser pingado: ")
        print('-' * 60)
        #chama a library os e executa o comando ping com os parametro -n com valor 6
        os.system('ping -n 6 {}'.format(ip_ou_host))
        print('-' * 60)


if __name__ == '__main__':
    ping = Ping()
    ping.pingar()