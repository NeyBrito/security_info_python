import itertools

string = input("Digite o texto a ser permutada: ")
resultado = itertools.permutations(string, len(string))

for i in resultado:
    print(''.join(i))