import os #Integra Programas e recursos do Sistema Operacional
import time



class Ping():
    def pingar(self):
        with open('../TCP/hosts.txt') as file:
            dump = file.read()
            dump = dump.splitlines()

            for ip in dump:
                print('Verificando o IP: ', ip)
                print('-' * 60)
                os.system('ping -n 2 {}' .format(ip))
                print('-' * 60)
                time.sleep(5)


if __name__ == '__main__':
    ping = Ping()
    ping.pingar()