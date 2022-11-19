import nomes
import time

letras = []

tema = input('Escolha o tema:\n1 - Animais\n2 - Objetos\nEscolha: ')

palavra = ""
if tema == "1":
    palavra = nomes.nome_animal()
elif tema == "2":
    palavra = nomes.nome_objeto()

espacos = list('_' * len(palavra))
saida = ' '.join(espacos)

tentativas = 6
tentativasn = 6

print("=========================================")
print('_ ' * len(palavra))
print("=========================================")

time.sleep(1)

print('Tentativas: {}'.format(tentativas))
print('Qual a palavra?')

time.sleep(1)

while "_" in espacos and tentativas > 0:
    letra = input('Escolha uma letra: ').lower().strip()
    time.sleep(1)
    if letra in letras:
        print("=========================================")
        print("Letra já escolhida anteriormente")
        print("=========================================")
    elif letra in palavra:
        while letra in palavra:
            pos = palavra.index(letra)
            espacos[pos] = letra.upper()
            saida = ' '.join(espacos)
            palavra = list(palavra)
            palavra[pos] = letra.upper()
            palavra = ''.join(palavra)
        print("=========================================")
        print(saida)
        print("=========================================")
    else:
        tentativas -= 1
        print("=========================================")
        print('Incorreto! Não há essa letra na palavra!\nTentativas restantes: {}\n{}'.format(tentativas, saida))
        print("=========================================")
    letras.append(letra)    


print('A palavra era {}'.format(palavra.upper()))
print("=========================================")
print("Fim")
