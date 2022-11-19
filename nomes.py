import random


def nome_animal():
    animal = ['abelha', 'avestruz', 'anta', 'arara' 'baleia', 'burro', 'borboleta', 'cabra', 'cachorro',
              'doninha', 'elefante', 'esquilo', 'ema', 'foca', 'flamingo', 'gato', 'galo', 'galinha', 'gafanhoto',
              'ganso', 'hamster', 'hiena', 'iguana', 'jumento', 'javali', 'joaninha', 'lagartixa', 'lobo',
              'macaco', 'minhoca', 'orangotango', 'ovelha', 'panda', 'pantera', 'pato', 'papagaio', 'quati', 'rato',
              'raposa', 'rinoceronte', 'raia', 'sapo', 'serpente', 'sardinha', 'tartaruga', 'tigre', 'tatu', 'tucano',
              'urso', 'vaca', 'vespa', 'veado', 'zebra']
    return random.choice(animal)


def nome_objeto():
    objeto = ['abajur', 'agulha', 'alfinete', 'algema', 'alicate', 'almofada', 'ampulheta', 'anel', 'antena', 'anzol',
              'apagador', 'apito', 'apontador', 'aspirador', 'banco', 'bandeira', 'bengala', 'bola', 'boneca',
              'borracha',
              'brinco', 'cadeado', 'lapis', 'prego']
    return random.choice(objeto)
