import random
import string



tamanho = int(input("Digite o tamanho da senha que você deseja: "))
chars = string.ascii_letters + string.digits + '!@#$%&*()-=+,.:;?'
rnd = random.SystemRandom() #os.urandom (Gera numero aleatorias a partir de fontes do SO)
print(''.join(rnd.choice(chars) for i in range(tamanho)))


