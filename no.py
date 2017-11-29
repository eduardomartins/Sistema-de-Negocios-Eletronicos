# coding: UTF-8

import collections


Ponto = collections.namedtuple('TRIA', ['p1', 'p2', 'p3'])

TAMANHOS = {
    'M1': Ponto(100, 200, 250),
    'M2': Ponto(100, 200, 300),
    'M3': Ponto(250, 400, 450),
    'M4': Ponto(1500, 2500, 3000),
    'M5': Ponto(1500, 2100, 2800),
    'M6': Ponto(400, 550, 800),
    'M7': Ponto(2000, 3000, 3500),
    'M8': Ponto(1800, 2000, 2300),
    'M9': Ponto(1500, 2100, 2800),
}



class No(object):
    def __init__(self, probablidade=None, tamanho=None):
        """  """

        if tamanho and not isinstance(tamanho, Ponto):
            raise Exception('O tamanho deve ser um tipo Ponto')

        self.tamanho = tamanho

        if probablidade and not(probablidade >= 0 and probablidade <= 1.0):
            raise Exception('O valor da probablidade está fora do intervalo válido')

        self.probabilidade = probablidade

    def __repr__(self):
        return 'No [%s, %s]' % (self.probabilidade, self.tamanho)

    def calcular(self):
        raise NotImplementedError

    def tempo(self):
        raise NotImplementedError

