import nomes
import time

tema = input('Escolha o tema:\n1 - Animais\n2 - Objetos\nEscolha: ')

if tema == "1":
    palavra = nomes.nome_animal()
elif tema == "2":
    palavra = nomes.nome_objeto()

espaços = list('_' * len(palavra))
saida = ' '.join(espaços)
#print(saida)
tentativas = 6
tentativasn = 6

print("=========================================")
print('_ ' * len(palavra))
print("=========================================")

time.sleep(1)

print('Tentativas: {}'.format(tentativas))
print('Qual a palavra?')

time.sleep(1)

while "_" in espaços and tentativas > 0:
    letra = input('Escolha uma letra: ').lower().strip()
    time.sleep(1)
    if letra in palavra:
        while letra in palavra:
            pos = palavra.index(letra)
            espaços[pos] = letra.upper()
            saida = ' '.join(espaços)
            palavra = list(palavra)
            palavra[pos] = letra.upper()
            palavra = ''.join(palavra)
        print("=========================================")
        print(saida)
        print("=========================================")
    else:
        tentativas -= 1
        print("=========================================")
        print('Incorreto! Não há essa letra na palavra!\n'
              'Tentativas restantes: {}\n{}'.format(tentativas, saida))
        print("=========================================")

print('A palavra era {}'.format((palavra).upper()))
print("=========================================")
